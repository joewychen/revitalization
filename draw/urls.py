# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('main/postprofile', views.postprofile, name='postprofile')
]
