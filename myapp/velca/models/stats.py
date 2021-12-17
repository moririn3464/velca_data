from typing import Callable
from django.db import models
from .player_name import Player_name

class Stats(models.Model):
  game_day = models.DateField(verbose_name='試合日')
  playername = models.ForeignKey(Player_name, on_delete=models.CASCADE, verbose_name='プレイヤー名')
  play_time = models.IntegerField('プレイタイム', default=0)
  score = models.IntegerField('得点', default=0)
  assist = models.IntegerField('アシスト数', default=0)
  rebound = models.IntegerField('リバウンド数', default=0)
  d_rebound = models.IntegerField('ディフェンスリバウンド数', default=0)
  o_rebound = models.IntegerField('オフェンスリバウンド数', default=0)
  steel = models.IntegerField('スティール数', default=0)
  block = models.IntegerField('ブロック数', default=0)

  def get_player_name(self):
    return "\n".join([p.name for p in self.playername.all()])
    
  class Meta:
    verbose_name = "スタッツ"
    verbose_name_plural = "スタッツ"

  def __str__(self):
    return str(self.playername)

    

