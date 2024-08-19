from django.shortcuts import render

def saudacao(request):
    return render(request, 'ola_mundo.html')

def comparacao(request):
    return render(request, 'index.html')

def definicao(request):
    return render(request, 'bug.html')
