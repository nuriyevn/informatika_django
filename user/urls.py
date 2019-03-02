from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all_users$', views.all, name='all'),
    url(r'rating$', views.rating, name='rating')
]
