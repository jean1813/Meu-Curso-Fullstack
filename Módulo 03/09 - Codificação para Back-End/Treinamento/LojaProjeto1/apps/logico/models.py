from django.db import models

class Firma(models.Model):
    nome = models.CharField("nome", max_length=50)
    emai = models.EmailField("email")
    foto = models.ImageField(upload_to="foto_perfil/")


    def __str__(self):
        return self.nome
    