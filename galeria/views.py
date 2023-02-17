from django.shortcuts import get_object_or_404, render

from galeria.models import Photographies

# Create your views here.
def index (request):
    photos = Photographies.objects.all().order_by("date").filter(published=True)
    search = request.GET.get("search", "")
    if search != "":
        print("SEARCH FOUND")
        photos = photos.filter(title__icontains=search)
    else:
        print("SEARCH NOT FOUND")

    return render(request, "index.html", {"data": photos})

def imagem (request, photo_id):
    photo = get_object_or_404(Photographies, pk=photo_id)
    return render(request, "imagem.html", {"photo": photo})