from django.shortcuts import render, redirect 
from django.contrib import messages

from .forms import UserRegisterForm

from .view_drf import *
# Create your views here.

def register(request):
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
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login... ')
            return redirect('user:login')
    else:
        form = UserRegisterForm()

    context = {
        'f_register': form,
        'next': request.POST.get('next') or request.GET.get('next')
    }
    return render(request, 'registration/register.html' , context)
