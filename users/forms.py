from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


class RegistrationForm(UserCreationForm):

    username=forms.CharField(label='User', min_length=5, max_length=10)
    password1=forms.CharField(widget=forms.PasswordInput, label='Password')
    password2=forms.CharField(widget=forms.PasswordInput, label='Repeat password')

    class Meta:
        model=User
        fields=['username', 'password1', 'password2']

    def username_clean(self):
        username=self.cleaned_data['username'].lower()
        new=User.Objects.filter(username=username)
        if new.count():
            raise ValidationError('User already exists')
        return username

    error_messages = {
        'password_mismatch': gettext_lazy("Passwords do not match"),
    }