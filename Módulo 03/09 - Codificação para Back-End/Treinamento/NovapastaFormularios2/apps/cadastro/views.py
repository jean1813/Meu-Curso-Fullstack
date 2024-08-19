from django.shortcuts import render, redirect
from .models import *
from .forms import *


def PgEstudante(request):
    # Define uma função chamada PgEstudante que recebe um parâmetro request. Essa função é uma view no contexto de um projeto Django.

    busca_estudantes = Estudante.objects.all() 
    # Aqui, está buscando todos os objetos da classe Estudante no banco de dados e armazenando na variável busca_estudantes.

    if request.method == "POST":
        # Verifica se o método do pedido HTTP é "POST". Isso é importante para saber se o formulário foi enviado.
        novo_estudante = FormularioEstudante(request.POST)
        # Se o método for "POST", cria uma instância do formulário FormularioEstudante preenchida com os dados enviados pelo usuário (disponíveis em request.POST).
        if novo_estudante.is_valid():
            # Verifica se o formulário é válido, ou seja, se todos os campos foram preenchidos corretamente conforme especificado no formulário.
            novo_estudante.save()
            # Se o formulário for válido, salva os dados no banco de dados.
            return redirect("pgestudante_inicial")
            # Após salvar os dados, redireciona o usuário para uma página chamada pgestudante_inicial.
    else:
        novo_estudante = FormularioEstudante()
        # Se o método do pedido HTTP não for "POST", cria uma instância vazia do formulário FormularioEstudante.

    return render(request, "index.html", {"formulario": novo_estudante, "estudantes": busca_estudantes})
    # Por fim, renderiza a página index.html, passando um dicionário de contexto com duas chaves: formulario, 
    # que contém a instância do formulário (preenchido ou vazio, dependendo do método), 
    # e estudantes, que contém a lista de todos os estudantes buscados anteriormente.

    # Essa view permite exibir um formulário para adicionar novos estudantes e também mostra a lista de todos os estudantes já cadastrados. 
    # Se um novo estudante for adicionado através do formulário, ele será salvo no banco de dados e a página será recarregada para refletir as mudanças.


def PgLista(request):
    busca_lista = Estudante.objects.all()
    return render(request, "lista.html", {"formulario": busca_lista, "estudantes": busca_lista})

