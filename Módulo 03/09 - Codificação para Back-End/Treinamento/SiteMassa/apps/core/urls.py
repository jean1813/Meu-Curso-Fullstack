from django.urls import path
from .views import *

urlpatterns = [
    path('', inicial, name= "pagina_inicial"),
    path('login', login, name= "pagina_login")
]

