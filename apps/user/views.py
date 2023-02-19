from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.shortcuts import redirect, render

from apps.user import forms

# Create your views here.
def login(request):
    form = forms.LoginForm()

    if "POST" in request.method:
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            email = form["email"].value()
            password = form["password"].value()

            user = auth.authenticate(
                request,
                username=email,
                password=password
            )

            if user is not None:
                auth.login(request, user)
                messages.success(request, "User logged in successfully")
                return redirect("index")
            messages.error(request, "Please, check your credentials and try again or create an account")
            redirect("login")
        else:
            messages.error(request, fill_form_message())

    return render(request, "login.html", {"form": form})


def register(request):
    form = forms.RegisterForm()

    if request.method == "POST":
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            password = form["password"].value()
            password_repeat = form["password_repeat"].value()

            if password != password_repeat:
                messages.error(request, "The informed passwords are not equal")
                return redirect("register")
            
            full_name = form["full_name"].value()
            first_name = get_first_name(full_name)
            last_name = get_last_name(full_name, first_name)
            email = form["email"].value()

            if User.objects.filter(email=email).exists():
                messages.error(request, "This e-mail is already registered. Try to log in or create another account")
                return redirect("register")
            
            user = User.objects.create_user(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, "Acount created successfully. You will now be redirected to login")
            return redirect("login")
        else:
            messages.error(request, fill_form_message())
    
    return render(request, "register.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "User logged out successfully")

    return redirect("login")


def get_first_name(full_name):
    first_name = ""

    for char in full_name:
        if char == " ":
            break
        first_name += char
    
    return first_name


def get_last_name(full_name, first_name):
    last_name = ""
    first_name += " "
    full_name = full_name.replace(first_name, "")

    for char in full_name:
        last_name += char

    return last_name


def fill_form_message():
    return "Please, fill in all the form fields correctly"