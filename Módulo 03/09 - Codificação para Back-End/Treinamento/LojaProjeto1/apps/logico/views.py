from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá Mundo !!!")

def mostra2(request):
    return HttpResponse("Resultado !!!")

def fisio(request):
    return HttpResponse("Recuperacao !!!")

def jogo(request):
    return HttpResponse("amostradinho")

def bug(request):
    return render(request,'ola_mundo.html')
