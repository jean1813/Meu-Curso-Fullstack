from django.db import models

class Instrutor(models.Model):
    nome = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    cpf = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    
