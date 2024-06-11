from django.db import models

class DadosPessoais(models.Model):
    rg = models.PositiveIntegerField()
