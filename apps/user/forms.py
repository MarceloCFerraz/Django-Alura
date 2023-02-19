
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

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        if full_name:
            full_name = full_name.strip()
            return full_name

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password and password_repeat:
            if password != password_repeat:
                raise forms.ValidationError('The typed passwords are not equal')
            else:
                return password_repeat