from django.shortcuts import render
from .views import *

def inicial(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

