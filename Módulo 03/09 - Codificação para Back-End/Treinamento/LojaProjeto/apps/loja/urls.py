from django.urls import path
from .views import saudacao, vamos, filho, html

urlpatterns = [
    path('apresentacao/', saudacao),
    path('vamos/', vamos),
    path('arthur/', filho),
    path('html/', html)

]
