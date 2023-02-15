from django.shortcuts import render

# Create your views here.
def index (request):
    data = {
        1: {
            "title": "Carina Nebulosa",
            "subtitle": "Shot from Nasa / James Webb"
        },
        2: {
            "title": "NGC 1659 Galaxy",
            "subtitle": "Shot from Nasa / Hubble"
        }
    }
    send = {"cards": data}
    return render(request, "index.html", send)

def imagem (request):
    return render(request, "imagem.html")