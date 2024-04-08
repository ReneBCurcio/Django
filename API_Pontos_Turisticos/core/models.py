from django.db import models
from atracoes.models import Atracao
from comentarios.models import comentario
from avaliacoes.models import avaliacoes
from enderecos.models import endereco

class ponto_turisticos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    aprovado = models.BooleanField()
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(comentario)
    avaliacao = models.ManyToManyField(avaliacoes)
    endereco = models.ForeignKey (endereco, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome