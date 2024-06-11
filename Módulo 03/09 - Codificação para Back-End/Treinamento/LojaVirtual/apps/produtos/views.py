from django.shortcuts import render
from .models import Produto

def VerProdutos(request):
    produtos_lista = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})

def Cadastro(request):
    return render(request, 'cadastro.html')

def Inicial(request):
    return render(request, 'inicial.html')
