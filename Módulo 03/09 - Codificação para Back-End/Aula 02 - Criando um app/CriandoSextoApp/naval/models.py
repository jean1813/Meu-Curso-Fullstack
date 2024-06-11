from django.db import models

class Major(models.Model):
    nome = models.CharField(max_length=50)
    
