from django.db import models

class Bug(models.Model):
    tipo_modelo = (
        ("AT", "atualizado"),
        ("M", "moderno")
    )
    nome = models.CharField("nome", max_length=20)
    email = models.EmailField("email")
    valor = models.DecimalField("valor",max_digits=4, decimal_places=2)
    modelo = models.CharField("modelo", max_length=4, choices=tipo_modelo)
    foto = models.ImageField(upload_to="foto_perfil/")

    class Meta:
        ordering = ('pk', )
        verbose_name = 'Bug'
        verbose_name_plural = 'Bugs'



    def __str__(self):
        return self.nome
    