from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name="login"),
    path('authenticate',views.authenticate,name="authenticate"),
    path('register',views.register,name="register"),
    path('sendRegister',views.sendRegister,name="sendRegister"),
    path('blog',views.blog,name='blog'),
    path('chart',views.chart,name='chart'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('toplibros',views.toplibros,name='toplibros'),
    path('unete',views.unete,name='unete')
]