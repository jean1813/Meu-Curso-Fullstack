from django.db import models
from .models import *

class Developer(models.Model):
    nome = models.CharField("nome",max_length=50)
    foto_prefil = models.ImageField(upload_to="foto-perfil/")


    def __str__(self):
        return self.nome
    
   
   