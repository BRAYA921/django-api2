from django.db import models

from django.db import models
from datetime import date

# Create your models here.
class libros(models.Model):
    titulo = models.CharField(max_length=50, default='')
    autor = models.CharField(max_length=50, default='')
    anio = models.DateField(default=date.today)


class prestamo(models.Model):
    prestamo = models.CharField(max_length=50)
    fecha_del_prestamo = models.DateField(max_length=50)
    

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_del_prestamo = models.DateField(max_length=50)
    libro_prestado = models.CharField(max_length=20)