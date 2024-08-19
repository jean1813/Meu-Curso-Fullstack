from django.urls import path
from .views import *

urlpatterns = [
    path("", VerPacientes, name="pagina_inicial"),
    path("ver_paciente/<int:id_produto>/", DetalhesPaciente, name="detalhes_paciente")
]