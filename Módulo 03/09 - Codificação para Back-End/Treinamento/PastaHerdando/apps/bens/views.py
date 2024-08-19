from django.shortcuts import render
from .models import *

def VerIndex(request):
    return render(request, 'index.html')

def VerLogin(request):
    return render(request, 'paginalogin.html')

def VerProdutos(request):
    return render(request, 'paginaprodutos.html')

def VerClientes(request):
    return render(request, 'paginaclientes.html')

def VerFornecedores(request):
    return render(request, 'paginafornecedores.html')

