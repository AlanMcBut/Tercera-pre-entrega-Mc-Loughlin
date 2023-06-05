from django.shortcuts import redirect, render
from .models import Video, Procesador, Mouse

def index(request):
    placas = Video.objects.all()
    lista_de_placas = {"placas":placas}
    return render(request, "producto/index.html", lista_de_placas)


def anuncio_placa(request):
    from .form import PlacaForm
    if request.method == "POST":
        form = PlacaForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect("producto:index")
    else:
        return render(request, "producto/crear_placa.html")
