from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def CriarEstudante(request):
    busca_estudantes = Estudante.objects.all()
    if request.method == "POST":
        novo_estudante = Estudante(request.POST)
        if novo_estudante.is_valid():
            novo_estudante.save()
            return redirect("pagina_inicial")
    else:
        novo_estudante = Estudante()
    return render(request, "pagina-estudantes.html", {"formulario": novo_estudante, "estudantes": busca_estudantes})

def CriarFormulario(request):
    busca_estudantes = FormularioEstudante.objects.all()
    if request.method == "POST":
        novo_estudante = FormularioEstudante(request.POST)
        if novo_estudante.is_valid():
            novo_estudante.save()
            return redirect("pagina_inicial")
    else:
        novo_estudante = Estudante()
    return render(request, "pagina-estudantes.html", {"formulario": novo_estudante, "estudantes": busca_estudantes})