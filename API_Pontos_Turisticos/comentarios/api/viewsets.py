from rest_framework.viewsets import ModelViewSet
from comentarios.models import comentario
from comentarios.api.serializers import ComentariosSerializer

class ComentariosViewSet(ModelViewSet):
    queryset = comentario.objects.all()
    serializer_class = ComentariosSerializer