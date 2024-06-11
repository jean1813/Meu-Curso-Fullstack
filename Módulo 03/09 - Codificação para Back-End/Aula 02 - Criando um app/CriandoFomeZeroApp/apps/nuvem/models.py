from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)


class Formas(models.Model):
    nome = models.CharField(max_length=30)
    descricacao = models.TextField()
    data_insercao = models.DateTimeField()
    quimico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
