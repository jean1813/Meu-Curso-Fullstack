from django.urls import path
from .views import *

urlpatterns = [
    path('', VerIndex),
    path('login', VerLogin),
    path('produtos', VerProdutos),
    path('clientes', VerClientes),
    path('fornecedores', VerFornecedores)
]