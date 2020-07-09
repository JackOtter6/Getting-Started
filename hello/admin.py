from django.contrib import admin

from .models import Greeting, Game

admin.site.register(Greeting)
admin.site.register(Game)