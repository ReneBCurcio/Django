from rest_framework.serializers import ModelSerializer
from comentarios.models import comentario

class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = comentario
        fields = ['id', 'usuario', 'comentario', 'data', 'aprovado']