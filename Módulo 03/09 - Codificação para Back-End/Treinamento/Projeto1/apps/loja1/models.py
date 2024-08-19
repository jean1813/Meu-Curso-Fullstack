from django.db import models


class Vendedor(models.Model):
    tipo_sexo = (
            ("Masculino", "Masculino"),
            ("Feminino", "Feminino")
    )

    nome = models.CharField(max_length=20, null=True, blank=True)
    foto = models.ImageField(upload_to="foto_perfil/", null=True, blank=True )
    idade_vendedor = models.CharField(max_length=30, null=True, blank=True)
    sexo = models.CharField(max_length=30, choices=tipo_sexo, null=True, blank=True)
    valor = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores' 

