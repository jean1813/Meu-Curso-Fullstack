from django.shortcuts import render
from django.http import HttpResponse

def saudacao (request):
    return HttpResponse("Olá Jean Carlos!!")

def vamos (request):
    return HttpResponse("vamos!!")

def filho (request):
    return HttpResponse("danado!!")

def html (request):
    return render(request,"index.html",{})



