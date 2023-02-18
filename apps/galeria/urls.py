from django.urls import path
import galeria.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("imagem/<int:photo_id>", views.imagem, name="imagem")
]