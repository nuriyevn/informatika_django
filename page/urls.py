from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^about$", views.about, name="about"),
    url(r"^news$", views.news, name="news"),
    url(r"^blogs$", views.blogs, name="blogs"),
    url(r"^discussions$", views.discussions, name="discussions"),
    url(r"^help$", views.help, name="help" ),
    url(r"^resource$", views.resource, name="resource"),
    url(r"^contact$", views.contact, name="contact")
]
