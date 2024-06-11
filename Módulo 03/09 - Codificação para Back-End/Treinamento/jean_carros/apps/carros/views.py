from django.shortcuts import render
from django.http import HttpResponse
from .models import Carro


def index_carros(request):
    return render(request, "ola_mundo.html")

def monza(request):
    return HttpResponse("monza!!")


def Vercarros(request):
    carros_lista = Carro.objects.all()
    return render(request, 'carros.html', {'carros': carros_lista})