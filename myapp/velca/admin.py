from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.core.checks.messages import CheckMessage
from django.db import models
from django.db.models import fields
from .models import Club, Player_personal, Stats, Game, Playername

# class GameAdmin(admin.ModelAdmin):
#   fields = ['get_playername', 'roster', 'home_club', 'away_club', ]
#   list_display = ['get_playername','roster', 'home_club', 'away_club',]

#   def get_playername(self, obj):
#     return "\n".join([p.name for p in obj.player_name.all()])


class StatsAdmin(admin.ModelAdmin):
  list_display = ['get_player_name']

  def get_player_name(self, obj):
      return "\n".join([p.name for p in obj.playername.all()])

myModels = [Club, Player_personal, Stats, Game, Playername]
admin.site.register(myModels)