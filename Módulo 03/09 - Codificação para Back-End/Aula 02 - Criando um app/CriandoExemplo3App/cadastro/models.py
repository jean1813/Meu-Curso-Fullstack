from django.db import models
class Documentos(models.Model):
    cpf = models.PositiveIntegerField()
    rg = models.PositiveIntegerField()
    email = models.EmailField()
    Data_nascimento = models.DateField()


