from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_de_funcionamento = models.TextField()
    idade_minima = models.IntegerField()

    def __str__(self):
        return self.nome
