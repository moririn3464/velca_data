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
  model = Stats
  list_display = ('game_day', 'player', 'get_club')

  def get_club(self, obj):
    return obj.player.players_team
  
  get_club.short_description = '所属クラブ'


class Player_personalAdmin(admin.ModelAdmin):
  model = Player_personal
  list_display = ('name', 'players_team')


class GameAdmin(admin.ModelAdmin):
  model = Game
  list_display = ('matchday', 'home_club', 'away_club')

myModels = [Club, Playername]
admin.site.register(myModels)
admin.site.register(Stats, StatsAdmin)
admin.site.register(Player_personal, Player_personalAdmin)
admin.site.register(Game, GameAdmin)
