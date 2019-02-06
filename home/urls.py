from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index3, name='index'),
]
