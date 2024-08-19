from django.urls import path
from .views import *


urlpatterns = [
    path("", LinkInicial, name="page_inicial"),
    path("estudantes", VerEstudantes, name="page_estudante"),
    path("professores", VerProfessores, name="page_professores"),
	path("funcionarios", VerFuncionarios, name="page_funcionarios"),	
]

