from django.forms import ModelForm
from django import forms

from users.models import User


class RegistrationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].unique = True

        self.fields['password'].required = True

        self.fields['username'].required = True
        self.fields['username'].unique = True

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'user_type']
        widgets = {
            'password': forms.PasswordInput({"class": "form-control", "placeholder":"Password"}),
            'email': forms.EmailInput({"class": "form-control", "placeholder":"Email"}),
            'username': forms.TextInput({"class": "form-control", "placeholder":"Username"}),
            'first_name': forms.TextInput({"class": "form-control", "placeholder": "FirstName"}),
            'last_name': forms.TextInput({"class": "form-control", "placeholder": "LastName"}),
        }
        help_texts = {
            'password': '* Password must be at least 6 characters long',
            'username': '* Username must be blah blah blah',
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput({"class": "form-control", "placeholder":"Username"}),
        max_length=80,
        label="Username",
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput({"class": "form-control", "placeholder":"Password"}),
        label="Password",
        required=True
    )