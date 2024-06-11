from django.db import models

class carro(models.Model):
    Marca_modelo = (
        ("F", "Fiat"),
        ("R","Renault"),
        ("W","Wolksvagem"),
        ("CH", "Chevrolet")
    )

    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=10)

    def __str__(self):
        return self.marca
        

    
class ramon(models.Model):
    Tipo_Sexo = (
        ("M", "Masculino"),
        ("F", "Feminino")    
    )
    
    sexo = models.CharField(max_length=2, choices=Tipo_Sexo)
    valor = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return self.sexo
    
    
