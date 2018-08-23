from django.db import models

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

class Reserva(models.Model):
    cantidad=models.IntegerField()
    estado=models.BooleanField(default=False)
    def __str__(self):
        return self.estado

class Libro(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.IntegerField()
    id_categoria=models.ForeignKey(Categoria,models.SET_NULL,blank=True, null=True)
    id_autor=models.ForeignKey(Autor,models.SET_NULL,blank=True, null=True)
    id_reserva=models.ForeignKey(Reserva,models.SET_NULL,blank=True, null=True)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombres= models.CharField(max_length = 100)
    correo = models.EmailField()
    password = models.CharField(max_length = 250)
    id_libro_fav=models.ForeignKey(Libro,models.SET_NULL,blank=True,null=True)
    id_reserva=models.ForeignKey(Reserva,models.SET_NULL,blank=True,null=True)
    id_autor_fav=models.ForeignKey(Autor,models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.nombres

class Descripcion_Venta(models.Model):
    cantidad=models.IntegerField()
    id_libro=models.ForeignKey(Libro,models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.cantidad

class Registro_Ventas(models.Model):
    total=models.FloatField()
    id_usuario=models.ForeignKey(Usuario,models.SET_NULL,blank=True,null=True)
    id_descripcion_venta=models.ForeignKey(Descripcion_Venta,models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.total

class Administrador(models.Model):
    usuario=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.usuario

class Contenido_Blog(models.Model):
    titulo = models.CharField(max_length=250, blank=True, null=True)
    contenido = models.CharField(max_length=250, blank=True, null=True)
    id_admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class Contenido_Evento(models.Model):
    titulo = models.CharField(max_length=250, blank=True, null=True)
    contenido = models.CharField(max_length=250, blank=True, null=True)
    fecha=models.DateField()
    id_admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class Suscripcion(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email