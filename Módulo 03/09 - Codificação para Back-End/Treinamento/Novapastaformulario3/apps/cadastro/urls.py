from django.urls import path
from .views import *

urlpatterns = [
    path("", CadastrarJogador, name="pagina_inicial"),
    path("pglista", PgListaJogadores, name="pglistajogadores")
]

