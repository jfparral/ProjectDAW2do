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
    path('unete',views.unete,name='unete'),
    path('mycsv.csv',views.csv,name='mycsv.csv'),
    path('comprar/<int:id>',views.comprar,name='comprar'),
    path('reservar/<int:id>',views.reservar,name='reservar')
]
