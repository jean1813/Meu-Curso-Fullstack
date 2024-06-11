from django.db import models

class Atualizacao(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.PositiveIntegerField()
    rg = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    email = models.EmailField()
    data_inclusao = models.DateField()

    def __str__(self):
        return self.nome
    
