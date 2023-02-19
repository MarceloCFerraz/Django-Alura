from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from galeria.models import Photographies

# Create your views here.
def index (request):
    if not request.user.is_authenticated:
        messages.error(request, "User not logged in. Redirecting to login page")
        return redirect("login")
    photos = Photographies.objects.all().order_by("date").filter(published=True)
    search = request.GET.get("search", "")
    if search != "":
        print("SEARCH FOUND")
        photos = photos.filter(title__icontains=search)
    else:
        print("SEARCH NOT FOUND")

    return render(request, "index.html", {"data": photos})

def imagem (request, photo_id):
    if not request.user.is_authenticated:
        messages.error(request, "User not logged in. Redirecting to login page")
        return redirect("login")
    photo = get_object_or_404(Photographies, pk=photo_id)
    return render(request, "imagem.html", {"photo": photo})