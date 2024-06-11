from django.db import models

class Vendedor(models.Model):
    tipo_genero = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("NB", "Não binario")
    )

    nome = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="foto_perfil/")
    ano_nascimento = models.PositiveIntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=4, choices=tipo_genero)

    class Meta:
        ordering =('pk',)
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"


    def __str__(self):
        return self.nome
