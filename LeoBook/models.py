from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido1 = models.CharField(max_length = 50)
    apellido2 = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.IntegerField(max_length = 30)
    descripcion = models.CharField(max_length = 250)
    fecha_publicacion = models.DateTimeField()
    precio = models.FloatField()
    autor = models.ManyToManyField(Autor)
    
    
    def __str__(self):
        return self.nombre

class User(models.Model):
    nombre= models.CharField(max_length = 100)
    user = models.CharField(max_length = 8)
    password = models.CharField(max_length = 12)
    rol = models.CharField(max_length=13)
    fecha_registro = models.DateTimeField()
    libros = models.ManyToManyField(Libro)
    autores = models.ManyToManyField(Autor)

class Compra(models.Model):
    precio_total = models.FloatField()
    fecha_emision = models.DateField()
    user = models.ManyToManyField(User)
    libros = models.ManyToManyField(Libro)


