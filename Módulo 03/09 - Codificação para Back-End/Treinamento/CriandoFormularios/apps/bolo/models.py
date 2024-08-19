from django.db import models

class Encomenda(models.Model):
    cliente = models.CharField(max_length=100)
    quant_bolos = models.PositiveIntegerField()

    def __str__(self):
        return self.cliente
