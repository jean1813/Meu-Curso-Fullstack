from django.shortcuts import render
from .models import *


def LinkInicial(request):
    return render(request, "index.html")


def VerEstudantes(request):
    VerEstudantes_lista = Estudante.objects.all()
    return render(request, 'estudantes.html', {'estudantes': VerEstudantes_lista})


def VerProfessores(request):
    VerProfessores_lista = Professor.objects.all()
    return render(request, "professor.html", {'professores': VerProfessores_lista})


def VerFuncionarios(request):
    VerFuncionarios_lista = Funcionario.objects.all()
    return render(request, "funcionarios.html", {'funcionarios': VerFuncionarios_lista})

