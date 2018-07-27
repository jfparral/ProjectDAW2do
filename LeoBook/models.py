from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido1=models.CharField(max_length=50)
    apellido2=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField(max_length=30)
    descripcion=models.CharField(max_length=250)
    fecha_publicacion=models.DateTimeField()
    libro=models.ManyToManyField(Autor)
    def __str__(self):
        return self.nombre