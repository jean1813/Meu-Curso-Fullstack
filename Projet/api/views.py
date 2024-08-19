from django.shortcuts import render
from rest_framework import generics, filters, serializers
from apps.core.models import Clientes
from .serializers import ClientesSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class PostListCreate(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields =  ["name", "cpf_cnpj", "rg_ie", "zip_code", "address", "neighborhood", "number", "city", "state" ]
    ordering_fields = ['created_at']

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ["name", "cpf_cnpj", "rg_ie", "zip_code", "address", "neighborhood", "number", "city", "state" ]
   
    def validate_title(self, value):
        if len(value) < 5:
         raise serializers.ValidationError("O título deve ter pelo menos 5 caracteres.")
        return value


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]