from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    posicao = models.CharField(max_length=50)
    estado_nascimento = models.CharField(max_length=50)
    anos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome 
    