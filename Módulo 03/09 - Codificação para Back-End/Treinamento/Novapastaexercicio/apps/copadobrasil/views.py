from django.shortcuts import render, redirect
from .models import *
from .forms import *


def VerIndex(request):
    buscar_resultados = Jogo.objects.all()  # Ou a lógica que você precisa
    return render(request, 'index.html', {'resultados': buscar_resultados})
    
    


def CriarTime(request):
    if request.method == "GET":
        novo_time = FormularioTime()
    else:
        Time_preenchido = FormularioTime(request.POST, request.FILES)
        if Time_preenchido.is_valid():
           Time_preenchido.save()
           return redirect("pg_index")
    return render(request, "criar_time.html", {"formulario_time": novo_time})


def CriarJogo(request):
    if request.method == "GET":
        novo_jogo = FormularioJogo()
    else:
        jogo_preenchido = FormularioJogo(request.POST, request.FILES)
        if jogo_preenchido.is_valid():
           jogo_preenchido.save()
           return redirect("pg_index")
    return render(request, "criar_jogo.html", {"formulario_jogo": novo_jogo})
