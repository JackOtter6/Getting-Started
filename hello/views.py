from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Game

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
def hangman(request):
    game = Game.objects.get(name="Hangman")
    return render(request, "GameTemplate.html", {"game":game})
def scrabble(request):
    game = Game.objects.get(name="Scrabble")
    return render(request, "GameTemplate.html", {"game":game})
def caesar_cipher(request):
    game = Game.objects.get(name="Caesar Cipher")
    return render(request, "GameTemplate.html", {"game":game})
def madlibs(request):
    game = Game.objects.get(name="MadLibs")
    return render(request, "GameTemplate.html", {"game":game})
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
