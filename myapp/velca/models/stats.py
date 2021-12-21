from typing import Callable
from django.db import models
from .playername import Playername
from .player_personal import Player_personal
from .game import Game

class Stats(models.Model):
  game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, related_name="game_stats")
  game_day = models.DateField(verbose_name='試合日')
  player = models.ForeignKey(Player_personal, on_delete=models.CASCADE, verbose_name='プレイヤー名')
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
    return str(self.player)

    

