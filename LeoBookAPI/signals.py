from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from LeoBookAPI.models import *
from LeoBookAPI.serializers import *
from ProjectDAW2do import settings
from django.core.mail import send_mail
import logging
stdlogger = logging.getLogger(__name__)

@receiver(post_save, sender='LeoBookAPI.Libro')
def run_before_saving(sender, **kwargs):
    var=str(kwargs.get('instance'))
    libro=Libro.objects.get(nombre=var)
    print(libro.stock)
    if libro.stock>0:
        reserva=Reserva.objects.all()
        for reserv in reserva:
            if libro.id==reserv.id_libro.get().id and reserv.estado==True:
                usuario=Usuario.objects.get(id=reserv.id_usuario.get().id)
                mail=str(usuario.correo)
                send_mail(
                    'Libro disponible',
                    'Su libro '+libro.nombre+' se encuentra en stock',
                    settings.EMAIL_HOST_USER,
                    [mail],
                    fail_silently=False,
                )
                reserv.estado=False
                reserv.save()