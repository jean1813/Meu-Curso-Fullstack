from django.db import models

class Biblia(models.Model):
    tipos_choices = (
        ("DE", "De Estudo"),
        ("C", "Cotidiano"),
        ("P", "Pesquisa")
        
    )

    titulo = models.CharField(max_length=20)
    quant_paginas = models.IntegerField()
    tipo = models.CharField(max_length=2, choices=tipos_choices)

    def __str__(self):
        return self.titulo
    
class Pastor(models.Model):
    teste_choices = (
        ("N1", "Teste Numero 1"),
        ("N2","Teste Numero 2"),
        ("N3","Teste Numero 3")
    )

    teste = models.CharField(max_length=10, choices=teste_choices )

    def __str__(self):
        return self.teste

class Igreja(models.Model):
    palestra_choices = (
        ("R", "Reconliciação"),
        ("F", "Futuro"),
        ("RL", "Resilencia")
    )

    palestra = models.CharField(max_length=20, choices=palestra_choices)

    def __str__(self):
        return self.palestra
       