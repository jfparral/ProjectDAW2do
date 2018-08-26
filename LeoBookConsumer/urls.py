from django.urls import path

from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('blog',views.blog,name='blog'),
    path('chart',views.chart,name='chart'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('toplibros',views.toplibros,name='toplibros'),
    path('unete',views.unete,name='unete')
]