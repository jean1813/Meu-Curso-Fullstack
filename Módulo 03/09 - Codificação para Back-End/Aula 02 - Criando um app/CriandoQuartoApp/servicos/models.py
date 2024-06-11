from django.db import models

class Tecnologia(models.Model):
    codigos = models.CharField(max_length=50)
    
