from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.CarroListView.as_view(), name='carro_list'), # Lista todos os carros (presumindo que você tenha uma visualização de lista)
    path('carro/<int:pk>/', views.CarroDetailView.as_view(), name='carro_detail'),  # Detalhes do carro
    path('carro/new/', views.CarroCreateView.as_view(), name='carro_create'),  # Cria um novo carro
    path('carro/<int:pk>/edit/', views.CarroUpdateView.as_view(), name='carro_update'), # Atualiza um carro existente
    path('carro/<int:pk>/delete/', views.CarroDeleteView.as_view(), name='carro_delete'), # Exclui um carro


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Passo 3: Certificar-se de Que as Visualizações e Modelos Estão Configurados
#Aqui está um resumo das visualizações que você configurou:

#CarroDetailView:
#URL: /carros/<id>/
#Template: carros/carro_detail.html
#Função: Exibe os detalhes de um carro.

#CarroCreateView:
#URL: /carros/create/
#Template: carros/carro_form.html
#Função: Exibe um formulário para criar um novo carro.

#CarroUpdateView:
#URL: /carros/<id>/update/
#Template: carros/carro_form.html
#Função: Exibe um formulário para atualizar um carro existente.

#CarroDeleteView:
#URL: /carros/<id>/delete/
#Template: carros/carro_confirm_delete.html
#Função: Exibe uma página de confirmação para excluir um carro.*/
