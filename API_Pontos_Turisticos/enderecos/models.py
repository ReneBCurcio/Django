from django.db import models

class endereco(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True )
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    latitude = models.IntegerField(null=True, blank=True) ##null, blank True deixa o campo como opcional
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
