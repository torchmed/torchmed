from django.conf.urls import patterns, url
from contact import views

urlpatterns = [
    url(r'^email/$', views.email, name='email'),
    url(r'^thanks/$',views.thanks, name='thanks'),
]
