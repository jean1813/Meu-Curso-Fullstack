from django.urls import path
from .views import *

urlpatterns = [
    path('', VerIndex),
    path('login', VerLogin),
    path('produtos', VerProdutos)
]
