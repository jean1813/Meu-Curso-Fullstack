from django.shortcuts import render
from django.http import HttpResponse

from .models import Vendedor

#def saudacao(request):
    #return HttpResponse("Olá mundo!!!")


#def saudacao(request):
    #return render(request, 'ola_jean.html')


#def VerVendedores(request):
    #vendedores_lista = Vendedor.objects.all()
    #return render(request, 'index.html', {'vendedores': vendedores_lista})

def LinkInicial(request):
    vendedores_lista = Vendedor.objects.all()
    return render(request, "index2.html", {'vendedores': vendedores_lista})

def LinkCadastro(request):
    return render(request, "cadastro.html")

