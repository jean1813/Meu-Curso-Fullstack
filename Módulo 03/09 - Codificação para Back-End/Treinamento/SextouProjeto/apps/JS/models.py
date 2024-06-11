from django.db import models

class var(models.Model):
    tipo_choices = (
        ("Python", "Python"),
        ("JavaScript", "JavaScript")
    )

    nome = models.CharField(max_length=20)
    tamanho = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=tipo_choices)

    def __str__(self):
        return self.tipo


class professor(models.Model):
    nome_choices = (
        ("Ramon", "Ramon"),
        ("G", "Glêssio")
    )
    nome = models.CharField(max_length=10, choices=nome_choices)

    def __str__(self):
        return self.nome
    

class PrecoMercadorias(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

class Meta:
    ordering = ('pk',)
    verbose_name = 'Preço Produto'
    verbose_name_plural = 'Preços Produtos'

