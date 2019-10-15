from typing import Type

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from wimperg.models import Profile


def get_form_error_list(form):
    errors = []
    for error_list in form.errors.values():
        for error in error_list:
            errors.append(error)
    return errors


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = self.fields['password2'].help_text = None
        self.fields['password1'].help_text = 'Min. 8 characters'


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'date_of_birth')
