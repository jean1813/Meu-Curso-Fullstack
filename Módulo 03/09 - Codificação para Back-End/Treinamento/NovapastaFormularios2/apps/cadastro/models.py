from django.db import models

class Estudante(models.Model):
    aluno = models.CharField(max_length=100)
    idade_aluno = models.PositiveIntegerField()
    quant_notas = models.PositiveIntegerField()

    def __str__(self):
        return self.aluno
