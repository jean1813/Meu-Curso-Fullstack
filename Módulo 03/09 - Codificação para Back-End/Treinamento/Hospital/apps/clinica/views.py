from django.shortcuts import render
from .models import *

def VerPacientes(request):
    pacientes_lista = Paciente.objects.all()
    return render(request, "lista-pacientes.html", {"pacientes": pacientes_lista})


def DetalhesPaciente(request, id_produto):
    busca = Paciente.objects.get(id=id_produto)
    return render(request, "detalhes-pacientes.html", {"paciente": busca})

