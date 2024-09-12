from django.urls import path
from .views import *
from apps.core import views

urlpatterns = [
    path('', views.CriarEstudante, name="pagina-estudantes.html"),
    path('', views.CriarFormulario, name="form.html"),
]