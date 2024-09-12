from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Carro

class CarroListView(ListView):
    model = Carro
    template_name = 'carros/carro_list.html'

class CarroDetailView(DetailView):  
    model = Carro
    template_name = 'carros/carro_detail.html'

class CarroCreateView(CreateView):
    model = Carro
    template_name = 'carros/carro_form.html'
    fields = ['modelo', 'foto', 'ano_fabricacao', 'acessorios', 'valor', 'tipo']
    success_url = reverse_lazy('carro_list')

class CarroUpdateView(UpdateView):
    model = Carro
    template_name = 'carros/carro_form.html'
    fields = ['modelo', 'foto', 'ano_fabricacao', 'acessorios', 'valor', 'tipo']

class CarroDeleteView(DeleteView):
    model = Carro
    template_name = 'carros/carro_confirm_delete.html'
    success_url = reverse_lazy('carro_list')

