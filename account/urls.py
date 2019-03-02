from django.conf.urls import  url
from . import views

app_name = 'account'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login_user_bla, name='login'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^dashboard$', views.dashboard, name='dashboard')
]
