from django.contrib import admin

from .models import Greeting, Game

class GameAdmin(admin.ModelAdmin):
    list_display=("name", "link",)

admin.site.register(Greeting)
admin.site.register(Game, GameAdmin)