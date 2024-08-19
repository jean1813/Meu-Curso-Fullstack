from django.shortcuts import render
from .models import *

def VerJogadores(request):
    jogadores_lista = Jogador.objects.all()
    return render(request, "lista-jogadores.html", {"jogadores": jogadores_lista})


def DetalhesJogador(request, id_produto):
    busca = Jogador.objects.get(id=id_produto)
    return render(request, "detalhes-jogadores.html", {"jogador": busca})
