from django.db import models

class Carro(models.Model):
    tipo_carro = (
        ("S", "Sedan"),
        ("H", "Hatch"),
        ("C", "Caminhonete")
    )

    modelo = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="foto_perfil/")
    ano_fabricacao = models.PositiveIntegerField()
    acessorios = models.TextField()
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    tipo = models.CharField(max_length=4, choices=tipo_carro)

    class Meta:
        ordering =('pk',)
        verbose_name = "Carro"
        verbose_name_plural = "Carros"


    def __str__(self):
        return self.modelo
    

    
