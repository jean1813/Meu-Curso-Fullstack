from django.db import models
from django.urls import reverse

class Carro(models.Model):
    tipo_carro = (
        ("SED", "Sedan"),
        ("SUV", "SUV"),
        ("HAT", "HATchback")
    )

    modelo = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="foto_perfil/")
    ano_fabricacao = models.PositiveIntegerField()
    acessorios = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    tipo = models.CharField(max_length=3, choices=tipo_carro)

    class Meta:
        ordering =('pk',)
        verbose_name = "Carro"
        verbose_name_plural = "Carros"


    def __str__(self):
        return self.modelo
    
    def get_absolute_url(self):
        return reverse('carro_detail', kwargs={'pk': self.pk})

    
