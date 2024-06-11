from django.urls import path

from .views import *

urlpatterns = [
    path('apresentacao/', saudacao),
    path('mostra-rota/', mostra2),
    path('fisio/', fisio),
    path('futebol/', jogo),
    path('close/', bug),
]