from djongo import models as djono_models

# Create your models here.
class Descripcion_Venta(djono_models.Model):
    cantidad=djono_models.IntegerField()
    libro=djono_models.CharField(max_length=50,blank=True,null=False)
    def __str__(self):
        return str(self.cantidad)

class Registro_Ventas(djono_models.Model):
    total=djono_models.FloatField()
    usuario=djono_models.CharField(max_length = 100)
    cantidad=djono_models.IntegerField()
    libro=djono_models.CharField(max_length=50)
    def __str__(self):
        return str(self.total)
    
class Reportes(djono_models.Model):
    usuario=djono_models.CharField(max_length = 100)
    libro=djono_models.CharField(max_length=50)
    cantidad=djono_models.IntegerField()
    total=djono_models.FloatField()
    objects = djono_models.DjongoManager()
    def __str__(self):
        return self.usuario
