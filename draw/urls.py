# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('app', views.datingapp, name='datingapp'),
    path('drawer', views.drawer, name='drawer'),
    path('textsender', views.textsender, name='textsender'),
    path('mainpage', views.mainpage, name='mainpage')
]
