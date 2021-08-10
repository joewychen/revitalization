# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('main/postprofile', views.postprofile, name='postprofile'),
    path('main/contest', views.contest, name='contest'),
    path('main/search', views.search, name='search'),
    path('main/post', views.post, name='post'),
    path('main/personal', views.personal, name = 'personal')
]
