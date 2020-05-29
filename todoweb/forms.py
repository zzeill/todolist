from django import forms
from .models import List, Activity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name',)


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'description',)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

