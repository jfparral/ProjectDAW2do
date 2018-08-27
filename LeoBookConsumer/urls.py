from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('indexUser',views.indexUser,name='indexUser'),
    path('login',views.login,name="login"),
    path('authenticate',views.authenticate,name="authenticate"),
    path('register',views.register,name="register"),
    path('sendRegister',views.sendRegister,name="sendRegister"),
    path('events',views.events,name='events'),
    path('eventsUser',views.eventsUser,name='eventsUser'),
    path('blog',views.blog,name='blog'),
    path('blogUser',views.blogUser,name='blogUser'),
    path('chart',views.chart,name='chart'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('nosotrosUser',views.nosotrosUser,name='nosotrosUser'),
    path('toplibros',views.toplibros,name='toplibros'),
    path('toplibrosUser',views.toplibrosUser,name='toplibrosUser'),
    path('unete',views.unete,name='unete'),
    path('mycsv.csv',views.csv,name='mycsv.csv'),
    path('myAnothercsv.csv',views.anothercsv,name='myAnothercsv.csv'),
    path('comprar/<int:id>',views.comprar,name='comprar'),
    path('reservar/<int:id>',views.reservar,name='reservar'),
    path('reservar/<int:id_user>/<int:id_book>',views.reservarUser,name='reservarUser'),
    path('comprar/<int:id_user>/<int:id_book>',views.comprarUser,name='comprarUser'),
    path('misreservas/<int:user>',views.misreservas,name='misreservas'),
    path('editarReserva/<int:user>/<int:id>',views.editarReserva,name='editarReserva'),
    path('eliminarReserva/<int:user>/<int:id>',views.eliminarReserva,name='eliminarReserva'),
    path('micuenta/<int:user>',views.micuenta,name='micuenta'),
    path('eliminarCuenta/<int:id>',views.eliminarCuenta,name='eliminarCuenta'),
    path('actualizarCuenta/<int:id>',views.actualizarCuenta,name='actualizarCuenta'),
]
