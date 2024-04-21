from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import Textarea , DateTimeField 

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import (Project, Asset, Step)

class UserRegisterForm(UserCreationForm):

    # email = forms.EmailField()
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']


class Project_Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'image']

class Asset_Form(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['project', 'name', 'description', 'file']

class Step_Form(forms.ModelForm):
    # TODO https://stackoverflow.com/questions/32015509/django-limit-the-choices-of-a-choice-field-in-a-form/32016091#32016091
    def __init__(self, *args, **kwargs):
        project = kwargs.get('project')

        assets = Asset.objects.all().order_by('name')

        if project:
            kwargs.pop('project')
            assets = assets.filter(course__project=project)

        super(Step_Form, self).__init__(*args, **kwargs)

        self.fields['steps'].choices = [(x.id, x.name) for x in assets]

    class Meta:
        model = Step
        fields = ['project', 'name', 'description', 'rank',
            'folder', 'file_path', 'asset', 'excerpt', 'excerpt_start',
            'excerpt_end' ]