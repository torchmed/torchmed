# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from dashboard import views

urlpatterns = [
    # URL pattern for the UserListView
    url(r'^$', views.index, name='dashboard'),
]

