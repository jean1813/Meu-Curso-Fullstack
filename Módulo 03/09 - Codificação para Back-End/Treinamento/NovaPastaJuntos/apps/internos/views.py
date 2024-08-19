from django.shortcuts import render
from .models import *

def PaginaInicial(request):
    return render(request, "index.html")

def PaginaPacientes(request):
    busca = Paciente.objects.all()

    
    return render(request, "lista-pacientes.html", {"pacientes": busca})
   
def PaginaDoutores(request):
    busca = Doutor.objects.all()
    return render(request, "lista-doutores.html", {"doutores": busca})

    