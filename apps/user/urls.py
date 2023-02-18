
from django.urls import path
import user.views as views


urlpatterns = [
    path("login.html", views.login, name="login"),
    path("register.html", views.register, name="register")
]
