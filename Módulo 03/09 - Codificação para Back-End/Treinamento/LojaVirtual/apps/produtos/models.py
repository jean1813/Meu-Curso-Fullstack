from django.db import models

class Produto(models.Model):

    TIPO_MAIOR_DE_IDADE = (
        ("Maior", "pode beber"),
        ("Menor", "não pode beber")
    )
    nome_produto = models.CharField("nome_do_produto",max_length=50)
    valor_produto = models.DecimalField("valor_produto", max_digits=5, decimal_places=2)
    imagem_do_produto = models.ImageField(upload_to="imagens/",null=True, blank=True)
    maior_de_idade = models.CharField(max_length=5, choices=TIPO_MAIOR_DE_IDADE, null=True, blank=True)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


    def __str__(self):
        return self.nome_produto
    

