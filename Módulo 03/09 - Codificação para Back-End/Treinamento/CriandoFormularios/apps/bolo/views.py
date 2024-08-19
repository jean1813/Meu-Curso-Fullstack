from django.shortcuts import render, redirect
from .models import *
from .forms import *


def PageInicial(request):
    busca_encomendas = Encomenda.objects.all()

    if request.method == "POST":
        nova_encomenda = FormularioEncomenda(request.POST)
        if nova_encomenda.is_valid():
            nova_encomenda.save()
            return redirect("pagina_inicial")
    else:
        nova_encomenda = FormularioEncomenda()

    return render(request, "index.html", {"formulario": nova_encomenda, "encomendas": busca_encomendas})
