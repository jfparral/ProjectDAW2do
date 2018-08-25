from django.urls import url

from . import views

urlpatterns = [
    url(r'^author/$', views.author_list),
    url(r'^category/$', views.category_list),
    url(r'^book/$', views.book_list),
    url(r'^booksell/(?P<user>[0-9]+)/(?P<book>[0-9]+)/$', views.book_sell),
    url(r'^user_reserve/(?P<user>[0-9]+)/(?P<book>[0-9]+)/$', views.book_reserve),
    url(r'^user_buy/(?P<user>[0-9]+)/$', views.user_detail_compras),
    url(r'^user_register/$', views.crear),
    url(r'^user_update/(?P<user>[0-9]+)/$', views.user_update),
    url(r'^user_delete/(?P<user>[0-9]+)/$', views.user_delete),
    url(r'^blog/$', views.blog_list),
    url(r'^blog_id/(?P<blog_id>[0-9]+)/$', views.blog_id),
    url(r'^event/$', views.event_list),
    url(r'^event_id/(?P<event_id>[0-9]+)/$', views.event_id),
]