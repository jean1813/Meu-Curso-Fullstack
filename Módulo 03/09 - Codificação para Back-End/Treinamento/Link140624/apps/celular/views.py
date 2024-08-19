from django.shortcuts import render
from django.http import HttpResponse
from .models import Marca

def saudacao(request):
    return HttpResponse("Olá PYTHON!!!")

def formacao(request):
    return render(request, 'index.html')
