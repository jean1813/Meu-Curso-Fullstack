from django.urls import path
from .views import * 

urlpatterns = [
    path("", VerIndex, name="pg_index"),
    path("criar-concurso", CriarConcurso, name="pg_formulario")
]
