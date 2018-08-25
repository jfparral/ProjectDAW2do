from django.urls import path

from . import views

urlpatterns = [
    path('prueba',views.index,name='index'),
    path('inicio',views.inicio,name="inicio"),
    path('blog',views.blog,name='blog'),
    path('chart',views.chart,name='chart'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('toplibros',views.toplibros,name='toplibros'),
    path('unete',views.unete,name='unete')
]