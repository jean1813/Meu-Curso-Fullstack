from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=20)
    valor_produto = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.nome_produto
    
class Mensagem(models.Model):
    nome_mensagem = models.CharField(max_length=30)
    valor_mensagem = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.nome_mensagem
    