from typing import Callable
from django.db import models

class Playername(models.Model):
  name = models.CharField('選手名', max_length=255)

  class Meta:
    verbose_name = "プレイヤー名"
    verbose_name_plural = "プレイヤー名"

  def __str__(self):
    return self.name
