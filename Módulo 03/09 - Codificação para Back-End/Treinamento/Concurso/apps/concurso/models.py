from django.db import models

class ConcursoUEMA(models.Model):
    titulo = models.CharField(max_length=100)
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    capa_concurso = models.ImageField(upload_to="fotos_capa")
    doc_edital = models.FileField(upload_to="edital_docs")

    def __str__(self):
        return self.titulo
