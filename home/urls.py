from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index3, name='index'),
    url(r'^lang$', views.lang, name='lang'),
    url(r'^change_locale/lang=(?P<lang>[a-zA-Z_]+)', views.change_locale, name='change_locale'),
]
