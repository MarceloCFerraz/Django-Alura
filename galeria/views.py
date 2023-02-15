from django.shortcuts import render

from galeria.models import Photography

# Create your views here.
def index (request):
    photos = Photography.objects.all()
    return render(request, "index.html", {"data": photos})

def imagem (request):
    return render(request, "imagem.html")