from .models import libros
from .models import prestamo
from .models import usuario

from rest_framework import viewsets,permissions
from .serializers import librosSerializer
from .serializers import prestamoSerializer
from .serializers import usuarioSerializer
from django_filters.rest_framework import DjangoFilterBackend

class librosViewSet(viewsets.ModelViewSet):
    queryset=libros.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=librosSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['titulo','autor']

class prestamoViewSet(viewsets.ModelViewSet):
    queryset=prestamo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=prestamoSerializer

class usuarioViewSet(viewsets.ModelViewSet):
    queryset=usuario.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=usuarioSerializer