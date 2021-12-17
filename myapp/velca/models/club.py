from django.db import models

class Club(models.Model):
  club_name = models.CharField('クラブ', max_length=255)

  def __str__(self):
      return self.club_name

  class Meta:
    verbose_name = "クラブ名"
    verbose_name_plural = "クラブ名"
