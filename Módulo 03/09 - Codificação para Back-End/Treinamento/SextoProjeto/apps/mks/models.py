from django.db import models

class Usuario(models.Model):
    tipos_choices = (
        ("R", "Revistas"),
        ("J", "Jornais"),
        ("I","Internet")
    )

    titulo = models.CharField(max_length=20)
    quant_paginas = models.IntegerField()
    tipo = models.CharField(max_length=2, choices=tipos_choices)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    

    def __str__(self):
        return self.titulo
    

class PrecoProdutos(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    nome = models.CharField(max_length=20, null=True, blank=True)
    ano_fabricacao = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Preço Produto'
        verbose_name_plural = 'Preços Produtos'
    
    def __str__(self):
        return self.valor