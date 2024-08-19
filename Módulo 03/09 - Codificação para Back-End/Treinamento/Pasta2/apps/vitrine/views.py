from django.shortcuts import render
from .models import Mensagem, Produto

def VerProdutos(request):
    produtos_lista = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})

def VerMensagens(request):
    mensagens_lista = Mensagem.objects.all()
    return render(request, 'msg.html', {'mensagem': mensagens_lista})

