from rest_framework import serializers
from LeoBookAPI.models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'fecha_nacimiento')

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('id', 'cantidad', 'estado')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'nombre', 'precio','id_categoria','id_autor','id_reserva')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombres', 'correo','password','id_libro_fav','id_reserva','id_autor_fav')

class DescripcionVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descripcion_Venta
        fields=('id','cantidad','id_libro')

class RegistroVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro_Ventas
        fields=('id','total','id_usuario','id_descripcion')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido_Blog
        fields = ('id', 'titulo', 'contenido')

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contenido_Evento
        fields=('id','titulo', 'contenido','fecha')

class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields=('id','email')