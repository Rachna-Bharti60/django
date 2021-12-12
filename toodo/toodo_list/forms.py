from django import forms
from django.forms import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import List
from toodo_list import models

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields =["item","completed"]
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']