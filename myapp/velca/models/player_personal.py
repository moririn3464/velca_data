from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from .player_name import Player_name
from .club import Club

class Player_personal(models.Model):
  name = models.OneToOneField(Player_name,on_delete=CASCADE, related_name="player_name")
  jersey_number = models.IntegerField(default=0,verbose_name='背番号')
  players_team = models.ForeignKey(Club, on_delete=models.CASCADE)


  class Meta:
    verbose_name = "プレイヤー情報"
    verbose_name_plural = "プレイヤー情報"

  def __str__(self):
    return str(self.name)
