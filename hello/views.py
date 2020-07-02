from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
def hangman(request):
    return render(request, "hangman.html")
def scrabble(request):
    return render(request, "scrabble.html")
def caesar_cipher(request):
    return render(request, "caesar_cipher.html")
def madlibs(request):
    return render(request, "madlibs.html")
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
