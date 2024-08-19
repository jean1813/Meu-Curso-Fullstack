from django.db import models

class clientes(models.Model):
    nome = models.CharField(max_length=30)
    sobre_nome = models.CharField(max_length=30)

    def __str__(self):
         return self.nome
    

class fornecedores(models.Model):
    nome = models.CharField(max_length=30)
    valor_produto = models.DecimalField(max_digits=2, decimal_places=10)

    def __str__(self):
         return self.nome
     
