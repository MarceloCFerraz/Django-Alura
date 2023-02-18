from django.shortcuts import render

from apps.user import forms

# Create your views here.
def login(request):
    form = forms.LoginForm()
    return render(request, "login.html", {"form": form})


def register(request):
    form = forms.RegisterForm()
    return render(request, "register.html", {"form": form})