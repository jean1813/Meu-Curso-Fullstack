from django.shortcuts import render
from django.http import HttpResponse

def LinkInicial(request):
    return render(request, "index.html")

def LinkCadastro(request):
    return render(request, "cadastro.html")
