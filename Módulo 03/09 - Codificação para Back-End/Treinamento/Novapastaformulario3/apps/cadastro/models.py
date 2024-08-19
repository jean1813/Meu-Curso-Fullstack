from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade_jogador = models.PositiveIntegerField()
    data_nasc = models.DateField()
    foto_perfil = models.ImageField(upload_to="foto_perfil/")
    documentos = models.FileField(upload_to="documentos/")
    posicao = models.CharField(max_length=50)
    time_atual = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    
