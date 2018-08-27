from django.conf.urls import url, include

from LeoBookAPI import views

urlpatterns = [
    url(r'^author/$', views.author_list.as_view()),
    url(r'^category/$', views.category_list.as_view()),
    url(r'^book_id/(?P<id>[0-9]+)/$', views.book_id.as_view()),
    url(r'^book/$', views.book_list.as_view()),
    url(r'^login_api/$',views.user_login.as_view()), 
    url(r'^register/$',views.registro_list.as_view()), 
    url(r'^description_sale/$',views.descripcion_venta_list.as_view()),
    url(r'^delete_reserve/(?P<id>[0-9]+)/$', views.eliminar_reserva.as_view()),
    url(r'^actualize_reserve/(?P<id>[0-9]+)/$',views.actualizar_reserva.as_view()),
    url(r'^reservar/(?P<id>[0-9]+)/$', views.reservar_id.as_view()),
    url(r'^booksell/(?P<user>[0-9]+)/(?P<book>[0-9]+)/$', views.book_sell.as_view()),
    url(r'^user_reserve/(?P<user>[0-9]+)/(?P<book>[0-9]+)/$', views.book_reserve.as_view()),
    url(r'^user_buy/(?P<user>[0-9]+)/$', views.user_detail_compras.as_view()),
    url(r'^user_id/(?P<id>[0-9]+)/$', views.user_id.as_view()),
    url(r'^user_register/$', views.crear.as_view()),
    url(r'^user_update/(?P<user>[0-9]+)/$', views.user_update.as_view()),
    url(r'^user_delete/(?P<user>[0-9]+)/$', views.user_delete.as_view()),
    url(r'^blog/$', views.blog_list.as_view()),
    url(r'^blog_id/(?P<blog_id>[0-9]+)/$', views.blog_id.as_view()),
    url(r'^events/$', views.event_list.as_view()),
    url(r'^event_id/(?P<event_id>[0-9]+)/$', views.event_id.as_view()),
]