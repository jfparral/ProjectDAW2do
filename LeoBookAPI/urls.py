from django.urls import url

from . import views

urlpatterns = [
    url(r'^author/$', views.author_list.asView()),
    url(r'^category/$', views.category_list.asView()),
    url(r'^book/$', views.book_list.asView()),
    url(r'^booksell/(?P<user>[0-9]+)/(?P<book>[0-9]+)/$', views.book_sell.asView()),
    url(r'^user_reserve/(?P<user>[0-9]+)/(?P<book>[0-9]+)/$', views.book_reserve.asView()),
    url(r'^user_buy/(?P<user>[0-9]+)/$', views.user_detail_compras.asView()),
    url(r'^user_register/$', views.crear.asView()),
    url(r'^user_update/(?P<user>[0-9]+)/$', views.user_update.asView()),
    url(r'^user_delete/(?P<user>[0-9]+)/$', views.user_delete.asView()),
    url(r'^blog/$', views.blog_list.asView()),
    url(r'^blog_id/(?P<blog_id>[0-9]+)/$', views.blog_id.asView()),
    url(r'^event/$', views.event_list.asView()),
    url(r'^event_id/(?P<event_id>[0-9]+)/$', views.event_id.asView()),
]