from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Post, Image

class PostForms(ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

class MyUserForm(UserCreationForm):
     class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']

class UserImage(ModelForm):
    class Meta:
        model = Image
        exclude = ['user']

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')

class UpdateUser(ModelForm):
    class Meta:
        model = Image
        fields = ['desc', 'image']
    

