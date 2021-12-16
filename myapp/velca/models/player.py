from typing import Callable
from django.db import models
from .club import Club

class Player(models.Model):
  name = models.CharField('選手名', max_length=255)
  jersey_number = models.IntegerField(default=0,verbose_name='背番号')
  players_team = models.ForeignKey(Club, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.name)
