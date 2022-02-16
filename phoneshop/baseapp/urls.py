"""
Baseapp urls 
""""

from django.urls import path

urlspatterns = [
    path (r'^$', views.index)
]