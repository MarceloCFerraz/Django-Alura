
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        required=True,
        label="Type your E-Mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "email@email.com"
            }
        ),
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        label="Type your Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "your password goes here"
            }
        )
    )


class RegisterForm(forms.Form):
    full_name = forms.CharField(
        required=True,
        max_length=100,
        label="Type your Full Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "your full name goes here"
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        label="Type your E-Mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "email@email.com"
            }
        ),
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        label="Type your Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "your password goes here"
            }
        )
    )
    password_repeat = forms.CharField(
        max_length=30,
        required=True,
        label="Type your Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "your password goes here"
            }
        )
    )