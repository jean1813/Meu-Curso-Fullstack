from django.db import models

class Equipamentos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano_fabricacao = models.DateField()
    descricao = models.TextField()
    

