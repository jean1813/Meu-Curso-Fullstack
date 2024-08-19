from django.urls import path
from .views import * 

urlpatterns = [
    path("", VerIndex, name="pg_index"),
    path("pg-time", CriarTime, name="formulario_time"),
    path("pg-jogo", CriarJogo, name="formulario_jogo"),
]