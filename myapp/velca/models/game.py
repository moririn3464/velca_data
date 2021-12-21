from typing import Callable
from django.db import models
from .club import Club
from .player_personal import Player_personal

class Game(models.Model):
  home_roster = models.ManyToManyField(Player_personal, related_name="home_roster")
  away_roster = models.ManyToManyField(Player_personal, related_name="away_roster")
  home_club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, related_name="home_club")
  away_club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, related_name="away_club")
  matchday = models.DateField(verbose_name='試合日')

  def __str__(self):
    return self.matchday.strftime('%Y/%m/%d')
    # return str(self.home_club)

  class Meta:
    verbose_name = "試合情報"
    verbose_name_plural = "試合情報"
