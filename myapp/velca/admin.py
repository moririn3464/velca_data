from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.core.checks.messages import CheckMessage
from django.db import models
from django.db.models import fields
from .models import Club, Player, Stats, Game

# class GameAdmin(admin.ModelAdmin):
#   list_display = ['get_playername','roster', 'home_club', 'away_club',]

#   def get_playername(self, obj):
#     return "\n".join([p.name for p in obj.player_name.all()])


myModels = [Club, Player, Stats, Game,]
admin.site.register(myModels)
