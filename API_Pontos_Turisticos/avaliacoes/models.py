from django.db import models
from django.contrib.auth.models import User

class avaliacoes(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True,blank=True)
    nota = models.DecimalField(decimal_places=1,max_digits=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
