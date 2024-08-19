from django.urls import path
from .views import *

urlpatterns = [
    path("", PgEstudante, name="pgestudante_inicial"),
    path("comeco", PgLista, name="pglista")
]