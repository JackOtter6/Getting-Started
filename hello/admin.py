from django.contrib import admin

from .models import Greeting, Game, Step

class StepInline(admin.TabularInline):
    model = Step
class GameAdmin(admin.ModelAdmin):
    list_display=("name", "link",)
    inlines = [StepInline,]
admin.site.register(Greeting)
admin.site.register(Game, GameAdmin)