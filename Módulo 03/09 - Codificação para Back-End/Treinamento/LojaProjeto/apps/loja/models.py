from django.db import models

class Produto(models.Model):
    nome = models.CharField("nome", max_length=50)
    preco = models.DecimalField("preco", decimal_places=2, max_digits=5)
    imagem = models.ImageField(upload_to="imagens/")
    manual = models.FileField(upload_to="pdfs/")

    def __str__(self):
        return self.nome
    

