from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Gratidão!!!")


def login(request):
    return HttpResponse("Vou contar pra sue pai, jean!!!")
