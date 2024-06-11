from django.db import models

class juizes(models.Model):
    Tipo_Atuacao = (
        ("C", "Criminal"),
        ("CV", "Civel"),
        ("P", "Previdenciario"),
        ("L", "Legislativo") 

    )
    
    nome = models.CharField(max_length=20)
    cpf = models.PositiveIntegerField()
    rg = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    email = models.EmailField()
    descricao = models.TextField()
    Area_Atuacao = models.CharField()
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nome
    
