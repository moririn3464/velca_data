from django.db import models

class Player(models.Model):
  player_name = models.CharField('選手名', max_length=255)
  play_time = models.IntegerField('プレイタイム', default=0)
  score = models.IntegerField('得点', default=0)
  assist = models.IntegerField('アシスト数', default=0)
  rebound = models.IntegerField('リバウンド数', default=0)
  d_rebound = models.IntegerField('ディフェンスリバウンド数', default=0)
  o_rebound = models.IntegerField('オフェンスリバウンド数', default=0)
  steel = models.IntegerField('スティール数', default=0)
  block = models.IntegerField('ブロック数', default=0)

  def __str__(self):
    return self.player_name