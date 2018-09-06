from rest_framework import serializers
from .models import *

class DescripcionVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descripcion_Venta
        fields=('id','cantidad','libro')

class RegistroVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro_Ventas
        fields=('id','total','usuario','cantidad','libro')
        
class ReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reportes
        fields=('id','usuario','libro','cantidad','total')
