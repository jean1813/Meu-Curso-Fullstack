from django.urls import path
from . import views



urlpatterns = [
    path('', views.ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', views.ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item-edit'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
    path('formulario/', views.FormularioView, name='formulario'),
    path('formulario/list/', views.FormListView, name='form-list'),
    path('formulario/<int:pk>/delete/', views.FormDeleteView, name='form-delete'),
    path('formulario/<int:pk>/', views.FormDetailView, name='form-detail'),
    path('formulario/<int:pk>/edit/', views.FormUpdatView, name='form-edit')
]
