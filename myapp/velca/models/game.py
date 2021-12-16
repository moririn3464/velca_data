from typing import Callable
from django.db import models
from .club import Club
from .player import Player
from .stats import Stats

class Game(models.Model):
  roster = models.ManyToManyField(Player)
  home_club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, related_name="home_club")
  away_club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, related_name="away_club")
  matchday = models.DateField(verbose_name='試合日')
  game_stats = models.ManyToManyField(Stats)

  def __str__(self):
    return self.matchday.strftime('%Y/%m/%d')