from django.urls import path
from .views import *

urlpatterns = [
    path('lista-produtos/', VerProdutos),
    path('mensagem_lista/', VerMensagens),
]

