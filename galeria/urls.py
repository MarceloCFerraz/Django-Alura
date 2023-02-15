from django.urls import path
import galeria.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("imagem/", views.imagem, name="imagem")
]