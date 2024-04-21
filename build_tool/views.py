import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse, resolve, Resolver404

from .forms import (UserRegisterForm, Project_Form, Asset_Form, Step_Form,)
from .view_drf import *
# Create your views here.

from functools import wraps
from django.http import HttpResponseRedirect

# + https://stackoverflow.com/questions/5469159/how-to-create-a-custom-decorator-in-django/6122181#6122181
def preserve_append_slash(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        resource = request.path
        # <<<<>>>>
        # Preserving effect of APPEND_SLASH
        # re_path(r'^(?!api|media|static).*$', views.index, name='remaining_urls') - see build_tool.url - inferferred with settings.APPEND_SLASH behaviour
        # e.g admin to admin/: 'admin' would show page_builder 404 page instead of redirecting to 'admin/'

        # + https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#resolve
        # add_leading_slash = f'/{resource}'
        add_leading_slash = resource
        try:
            match = resolve(add_leading_slash)
            # Print the URL pattern that matches the URL
            # print(match.url_name)
            print(match.view_name)
            if 'build_tool' in match.view_name: # build_tool:build_tool_index
                raise Resolver404()
            
        except Resolver404 as e:
            # check if it has a slash '/' already
            if settings.APPEND_SLASH and resource[-1] != "/":
                # Now add trailing slash '/'
                if request.GET:
                    # without this url like '/user/api/otl?uid=a14d6647-58d3-4d6a-90cb-d6ad38f47121&next=/my_profile' are affected
                    add_trailing_slash = f'{add_leading_slash}/?{request.GET.urlencode()}'
                else:
                    add_trailing_slash = f'{add_leading_slash}/'
                    
                try:
                    match = resolve(add_trailing_slash)
                    # Print the URL pattern that matches the URL
                    # print(match.url_name)
                    return redirect(add_trailing_slash)
                except Resolver404 as e:
                    print(f'No view function found "{add_trailing_slash}"')
                    pass
        # <<<<>>>>

        return function(request, *args, **kwargs)

  return wrap

@preserve_append_slash
@login_required
def index(request):
    context = {}

    return render( request, 'build_tool_vue/dist/index.html', context)

def install(request):
    if not os.path.exists("INSTALL_NJOGUSH"):
        messages.info(request, f'The installtion script has already been run')
        return redirect('build_tool:index')

    # TODO https://docs.djangoproject.com/en/4.0/ref/views/#the-403-http-forbidden-view
    # raise PermissionDenied # temporarily suspending sign ups as the system is still on the internet even during development

    if request.method == 'POST':
        # email will be populated from username once verified in 'verification' application
        form = UserRegisterForm(request.POST)
        # This option was withdrawn because the form doesn't have first & last name, email fields
        # hence doesn't prepopulate the UI form incase of validation error 
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')

            if os.path.exists("INSTALL_NJOGUSH"):
                os.remove("INSTALL_NJOGUSH")
            else:
                print("The file 'INSTALL_NJOGUSH' does not exist")

            messages.success(request, f'Your account has been created! You can now login... ')
            return redirect('user:login')
    else:
        form = UserRegisterForm()

    context = {
        'f_register': form,
        'next': request.POST.get('next') or request.GET.get('next')
    }
    return render(request, 'registration/register.html' , context)