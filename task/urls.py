from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all_tasks$', views.all, name='all'),
    url(r'^statistics$', views.statistics, name='statistics'),
    url(r'^results$', views.results, name='result'),
]
