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
    print("Start pre_save Item in signals.py under items app")
    print("sender %s" % (sender))
    print("kwargs %s" % str(kwargs))
    var=str(kwargs.get('instance'))
    libro=Libro.objects.get(nombre=var)
    print(libro.stock)
    if libro.stock>0:
        reserva=Reserva.objects.all()
        print("Mas de 0")
        for reserv in reserva:
            #print("Reservas",reserv)
            #print("Libro",libro.id)
            #print("Reserva",reserv.id_libro.get().id)
            #print(reserv.cantidad)
            if libro.id==reserv.id_libro.get().id:
                print("id igual")
                usuario=Usuario.objects.get(id=reserv.id_usuario.get().id)
                mail=str(usuario.correo)
                print(mail)
                send_mail(
                    'Libro disponivle',
                    'Su libro '+libro.nombre+' se encuentra en stock',
                    settings.EMAIL_HOST_USER,
                    [mail],
                    fail_silently=False,
                )
                reserv.estado=False
                reserv.save()
                serializer = ReservaSerializer(reserv)
                if serializer.is_valid():
                    serializer.save()
                    print("Posi")

    """
    stdlogger.info("Start pre_save Item in signals.py under items app")
    stdlogger.info("sender %s" % (sender))
    stdlogger.info("kwargs %s" % str(kwargs))
    """