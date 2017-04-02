from django.conf.urls import include, url
from contact import views

urlpatterns = [
    url(r'^email/$', views.email, name='email'),
    url(r'^thanks/$',views.thanks, name='thanks'),
]
