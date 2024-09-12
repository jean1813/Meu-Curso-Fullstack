from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendedor


def index_vendedor(request):
    return render(request, "vendedor.html")

def monza(request):
     return render(request, "carros.html")


def Vervendedores(request):
    vendedores_lista = Vendedor.objects.all()
    return render(request, 'vendedor.html', {'vendedores': vendedores_lista})



