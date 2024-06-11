from django.urls import path
from .views import *

urlpatterns = [
    path('lista-produtos/', VerProdutos, name="verprodutos" ),
    path('cadastro/', Cadastro, name="cadastro"),
    path('inicial/', Inicial, name="inicial"),
]
