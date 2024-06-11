from .views import *
from django.urls import path


urlpatterns = [
    path("", index_carros),
    path("monza/", monza),
    path("vercarros/", Vercarros)
]


