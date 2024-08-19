from django.db import models

class Estudante(models.Model):

    TIPO_SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )

    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=30)
    foto = models.ImageField(upload_to="foto_perfil/")
    escolaridade = models.CharField(max_length=30)
    nota = models.DecimalField(max_digits=10, decimal_places=2)
    ano_inicio = models.DateField()
    ano_conclusao = models.DateField()
    sexo = models.CharField(max_length=2, choices=TIPO_SEXO)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'


class Funcionario(models.Model):

    TIPO_SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )

    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=30)
    foto = models.ImageField(upload_to="foto_perfil/")
    sexo = models.CharField(max_length=2, choices=TIPO_SEXO)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'



class Professor(models.Model):

    TIPO_SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )

    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=30)
    foto = models.ImageField(upload_to="foto_perfil/")
    sexo = models.CharField(max_length=2, choices=TIPO_SEXO)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
