# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def main(request):
    return render(request, 'draw/main.html')

def postprofile(request):
    return render(request, "draw/postprofile.html")

def contest(request):
    return render(request, "draw/contest.html")
def search(request):
    return render(request, "draw/search.html")
def post(request):
    return render(request, "draw/post.html")

def personal(request):
    return render(request, "draw/personal.html")