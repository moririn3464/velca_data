from typing import List
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Player, Club, Stats, Game

def index(request):
  return render(request, 'velca/index.html')


class PlayerListView(ListView):
  model = Player


class GameDataView(ListView):
  template_name = 'velca/game_data.html'
  model = Game

  def get_context_data(self, **kwargs):
    context = super(GameDataView, self).get_context_data(**kwargs)
    context.update({
      # 試合情報用フィルター
      'player_list': Player.objects.all(),
      'home_player': Player.objects.filter(players_team='1').all(),
      'away_player': Player.objects.exclude(players_team='1').all(),
      'stats_list': Stats.objects.all(),
      'home_player_stats_list': Stats.objects.filter(player_name__players_team='1').all(),
      'away_player_stats_list': Stats.objects.exclude(player_name__players_team='1').all(),
    })  
    return context
