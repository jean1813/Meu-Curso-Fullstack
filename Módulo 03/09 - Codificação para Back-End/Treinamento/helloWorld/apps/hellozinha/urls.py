from django.urls import path
from .views import *

urlpatterns = [
    path('rota-saudacao', saudacao),
    path('rota-comparacao', comparacao),
    path('rota-definicao', definicao)
]