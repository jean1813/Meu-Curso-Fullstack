from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    diagnostico = models.CharField(max_length=100)
    exame_solicitado = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome   
