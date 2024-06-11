from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendedor


def index_vendedor(request):
    return render(request, "ola_vendedor.html")

def monza(request):
    return HttpResponse("monza!!")


def Vervendedores(request):
    vendedores_lista = Vendedor.objects.all()
    return render(request, 'vendedor.html', {'vendedores': vendedores_lista})



