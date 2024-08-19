from django.shortcuts import render, redirect
from .models import *
from .forms import *

def CadastrarJogador(request):

    busca_jogadores = Jogador.objects.all()

    if request.method == "POST":
        novo_jogador = FormularioJogador(request.POST)
        if novo_jogador.is_valid():
            novo_jogador.save()
            return redirect("pagina_inicial")
    else:
        novo_jogador = FormularioJogador()

    return render(request, "pagina-jogador.html", {"formulario": novo_jogador, "estudantes": busca_jogadores})

def PgListaJogadores(request):
    busca_lista = Jogador.objects.all()
    return render(request, "lista_jogadores.html", {"jogadores": busca_lista})

