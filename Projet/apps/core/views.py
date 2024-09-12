from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from .models import Clientes
from django.db.models import F
from .forms import ClientesForm
from datetime import datetime
from django.contrib import messages

class ItemListView(ListView):
    model = Item
    success_url = '/'
    template_name = 'item/item_list.html'


class ItemDetailView(DetailView):
    model = Item
    success_url = '/'
    template_name = 'item/item_detail.html'


class ItemCreateView(CreateView):
    model = Item
    fields = ['nome', 'descricao', 'preco']
    success_url = '/'
    template_name = 'item/item_form.html'


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['nome', 'descricao', 'preco']
    success_url = '/'
    template_name = 'item/item_form.html'


class ItemDeleteView(DeleteView):
    model = Item
    success_url = '/'
    template_name = 'item/item_confirm_delete.html'


def FormularioView(request):
    if request.method == "POST":
       form = ClientesForm(request.POST or None)
       if form.is_valid():
           # Porcessar os dados do fomulário
           # nome = form.cleaned_data['nome']
           # email = form.cleaned_data['email']
           # mensagem = form.cleaned_data['mensagem']
           # Adicione sua lógica aqui (e.g., salvar no banco de dados.)

           cd = form.cleaned_data
           pd = Clientes(
               name = cd ['name'],
               cpf_cnpj = cd ['cpf_cnpj'],
               rg_ie = cd ['rg_ie'],
               zip_code = cd ['zip_code'],
               address = cd ['address'],
               neighborhood = cd ['neighborhood'],
               number = cd ['number'],
               city = cd ['city'],
               state = cd ['state'],
               ddd = "",
               created_at = datetime.now(),
               # updated_at = 'null',
               # deleted_at = 'null',
           )
           pd.save()
           #messages.debug(request, "%s SQL statements were executed." count)
           #messages.info(request, "There credits remain in your")
           messages.success(request, "Dados adicionados com sucesso no Formulário.")
           return redirect('formulario')
       else:
           print(form.errors)
    else:
        form = ClientesForm()
    return render(request, 'forms/form_template.html', {'form': form})


def FormListView(request):
    client = Clientes.objects.all()
    return render(request, 'forms/form_list.html', {'client':client})


def FormDeleteView(request, pk):
    id = pk 
    client = Clientes.objects.get(pk=id)

    if request.method == "POST":
        client.delete()
        messages.success(request, "Cliente deletado com sucesso!.")
        return redirect('form-list') 
    return render(request, 'forms/form_confirm_delete.html', {'client': client})

def FormUpdatView(request, pk):
    id = pk
    # pega o objeto que veio do template pela primari key
    # client = Clientes.objects.get(pk=id)#
    client = get_object_or_404(Clientes, pk=id)
    # inicia função se o metodo for post
    if request.method =="POST":
        # Criamaos as novas variáveis com os novos rigistros vindo do formulário
        name = request.POST.get('name'),
        cpf_cnpj = request.POST.get('cpf_cnpj'),
        rg_ie = request.POST.get('rg_ie'),
        zip_code = request.POST.get('zip_code'),
        address = request.POST.get('address'),
        neighborhood = request.POST.get('neighborhood'),
        number = request.POST.get('number'),
        city = request.POST.get('city'),
        state = request.POST.get('state'),
        # creatd_at="",
        # updated_at = datetime.now(),
        # updated_at ='null',

        # joga os novos registros dentro da tabela
        client.name = name
        client.cpf_cnpj = cpf_cnpj
        client.rg_ie = rg_ie
        client.zip_code = zip_code
        client.address = address
        client.neighborhood = neighborhood
        client.number = number
        client.city  = city 
        client.state = state
        # client.updated_at = updated_at
        # continue para outros campos

        # salva os novos registros na tabela
        client.save()
        # messages.debug(request, "%s SQL statements were executed." count)
        # messages.info(request, "There credits remain in your")
        messages.success(request, "Dados atualizados com sucesso no Formulário.")
        # messages.warning(request, "your account")
        # messages
        return redirect('formulario')
    return render(request, 'forms/form_edit.html', {'client': client})


def FormDetailView(request, pk):
    id = pk 
    client = Clientes.objects.get(pk=id)   
    return render(request, 'forms/form_detail.html', {'client': client})


   
    
    





















