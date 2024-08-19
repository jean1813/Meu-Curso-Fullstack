from django.shortcuts import render, redirect
from .models import *
from .forms import *


def VerIndex(request):
    busca_concurso = ConcursoUEMA.objects.all()
    return render(request, "index.html", {"concursos":busca_concurso})


def CriarConcurso(request):
    if request.method == "GET":
        novo_concurso = FormularioVerconcursoUEMA()
    else:
        concurso_preenchido = FormularioVerconcursoUEMA(request.POST, request.FILES)
        if concurso_preenchido.is_valid():
           concurso_preenchido.save()
           return redirect("pg_index")
    return render(request, "criar-concurso.html", {"formulario": novo_concurso})
