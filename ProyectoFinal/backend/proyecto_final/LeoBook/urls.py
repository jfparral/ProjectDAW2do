from django.conf.urls import url, include
from LeoBook import views

urlpatterns = [
    url(r'^index/$',views.EventoListar.as_view(),name='indice'),
    url(r'^administrador/$',views.EventoListar.as_view(),name='listar_usuarios'),
]