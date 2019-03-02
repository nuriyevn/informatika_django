from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^active$', views.active, name='active'),
    url(r'^planned$', views.planned, name='planned'),
    url(r'^history$', views.history, name='history')
]
