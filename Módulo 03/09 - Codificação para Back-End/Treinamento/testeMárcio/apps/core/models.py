from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="foto/perfil")
    
    def __str__(self):
        return self.nome