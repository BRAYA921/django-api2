from rest_framework import serializers
from .models import libros, prestamo, usuario

class librosSerializer(serializers.ModelSerializer):
    class Meta:
        model=libros
        fields= '_all_'

class prestamoSerializer(serializers.ModelSerializer):
    class Meta:
      model=prestamo
      fields = '_all_'

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
      model=usuario
      fields = '_all_'