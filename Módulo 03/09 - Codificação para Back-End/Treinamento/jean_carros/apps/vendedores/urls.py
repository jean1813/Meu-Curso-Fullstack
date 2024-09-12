from .views import *
from django.urls import path


urlpatterns = [
    path("", index_vendedor),
    path("monza/", monza),
    path("vendedores/", Vervendedores)
]