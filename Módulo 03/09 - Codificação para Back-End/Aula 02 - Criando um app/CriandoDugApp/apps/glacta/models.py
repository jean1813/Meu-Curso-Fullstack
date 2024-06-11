from django.db import models

class jogos(models.Model):
    nome = models.CharField(max_length=30)
    data_fabricacao = models.DateField()
    descricacao = models.TextField()
    criador = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    