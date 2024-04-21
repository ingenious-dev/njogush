from django  import forms 

from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    # email = forms.EmailField()
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']

