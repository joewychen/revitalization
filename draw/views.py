# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def main(request):
    return render(request, 'draw/main.html')

def postprofile(request):
    return render(request, "draw/postprofile.html")