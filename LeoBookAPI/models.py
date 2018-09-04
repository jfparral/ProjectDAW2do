from django.db import models
from djongo import models as djono_models
# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_nacimiento=models.DateField()
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.FloatField()
    stock=models.IntegerField()
    id_categoria=models.ManyToManyField(Categoria)
    id_autor=models.ManyToManyField(Autor)
    image = models.ImageField(upload_to='static/img/',blank=True, null=True)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombres= models.CharField(max_length = 100)
    correo = models.EmailField()
    password = models.CharField(max_length = 250)
    is_staff=models.BooleanField(default=True)
    id_libro_fav=models.ManyToManyField(Libro)
    id_autor_fav=models.ManyToManyField(Autor)
    def __str__(self):
        return self.nombres

class Reserva(models.Model):
    cantidad=models.IntegerField()
    estado=models.BooleanField(default=False)
    id_libro=models.ManyToManyField(Libro)
    id_usuario=models.ManyToManyField(Usuario)
    def __str__(self):
        return str(self.id_libro.get().nombre)

class Descripcion_Venta(djono_models.Model):
    cantidad=djono_models.IntegerField()
    libro=djono_models.CharField(max_length=50)
    def __str__(self):
        return str(self.cantidad)

class Registro_Ventas(djono_models.Model):
    total=djono_models.FloatField()
    usuario=djono_models.CharField(max_length = 100)
    cantidad=djono_models.IntegerField()
    libro=djono_models.CharField(max_length=50)
    def __str__(self):
        return str(self.total)

class Contenido_Blog(models.Model):
    titulo = models.CharField(max_length=250, blank=True, null=True)
    contenido = models.CharField(max_length=5000,blank=True, null=True)
    autor = models.CharField(max_length=100,blank=False, null=True)
    fecha = models.DateField(blank=False, null=True)
    image = models.ImageField(upload_to='static/img/',blank=True, null=True)
    def __str__(self):
        return self.titulo

class Contenido_Evento(models.Model):
    titulo = models.CharField(max_length=250, blank=True, null=True)
    contenido = models.CharField(max_length=5000,blank=True, null=True)
    fecha=models.DateField()
    image = models.ImageField(upload_to='static/img/',blank=True, null=True)
    def __str__(self):
        return self.titulo

class Suscripcion(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email

class Administrador(models.Model):
    usuario=models.CharField(max_length=50,blank=True,null=False)
    contrasena=models.CharField(max_length=50,blank=True,null=False)
    def __str__(self):
        return self.usuario

class Reportes(djono_models.Model):
    usuario=djono_models.CharField(max_length = 100)
    libro=djono_models.CharField(max_length=50)
    cantidad=djono_models.IntegerField()
    total=djono_models.FloatField()
    objects = djono_models.DjongoManager()
    def __str__(self):
        return self.usuario
