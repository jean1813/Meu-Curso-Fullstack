from django.urls import path
from .views import *

urlpatterns = [
    path("", PageInicial, name="pagina_inicial")
]
