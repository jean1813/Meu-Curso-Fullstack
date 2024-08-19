from django.db import models

tipo_modelo = (
        ("A", "Android"),
        ("I", "Iphone")
    )

class Marca(models.Model):
    nome_marca = models.CharField(max_length=20)
    valor_marca = models.DecimalField(decimal_places=2, max_digits=6)
    modelo = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="foto_perfil/")
    
    def __str__(self):
        return self.nome
    

