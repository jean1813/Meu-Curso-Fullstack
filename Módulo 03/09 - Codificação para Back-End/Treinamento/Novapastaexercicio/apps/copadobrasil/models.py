from django.db import models

class Time(models.Model):
    nome_time = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_time
    
    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"
    

class Jogo(models.Model):
    time1 = models.ForeignKey(Time, related_name='time1_jogos', on_delete=models.CASCADE)
    placar_time1 = models.IntegerField()
    time2 = models.ForeignKey(Time, related_name='time2_jogos', on_delete=models.CASCADE)
    placar_time2 = models.IntegerField()

    def __str__(self):
        return f"{self.time1} vs {self.time2}"
    
    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"
    