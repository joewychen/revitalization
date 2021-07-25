# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def datingapp(request):
    return render(request, 'draw/datingapp.html')

def drawer(request):
    return render(request, 'draw/drawer.html')

def textsender(request):
    return render(request, 'draw/textsender.html')

def mainpage(request):
    return render(request, 'draw/mainpage.html')