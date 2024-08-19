from django.urls import path
from .views import *

urlpatterns = [
    path("", VerJogadores, name="pagina_inicial"),
    path("ver_jogador/<int:id_produto>/", DetalhesJogador, name="detalhes_jogador")
]