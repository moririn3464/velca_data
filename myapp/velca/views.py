from typing import List
from django.http import request
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Player_personal, Club, Stats, Game

def index(request):
  return render(request, 'velca/index.html')


class PlayerListView(ListView):
  model = Player_personal


class GameDataView(ListView):
  template_name = 'velca/game_data.html'
  model = Game

  # def get_context_data(self, **kwargs):
  #   context = super(GameDataView, self).get_context_data(**kwargs)
  #   context.update({
  #     # 試合情報用フィルター
  #     'velca_stats': Game.objects.filter(home_roster__players_team__club_name='長崎ヴェルカ'),
  #     'stats_list': Stats.objects.all(),
  #   })  
  #   return context


def game_detail(request, game_id):
  game_detail = Game.objects.get(id=game_id)
  game_stats = game_detail.game_stats.all()
  velca_stats = game_detail.game_stats.filter(player__players_team=1)
  opponent_stats = game_detail.game_stats.filter(player__players_team=2)
  # def get_context_data(self, **kwargs):
  #   context = super(game_detail, self).get_context_data(**kwargs)
  #   context.update({
  #       # 試合情報用フィルター
  #       'velca_stats': game_detail.game_stats.all,
  #   })
  #   return context

  return render(request, 'velca/game_detail.html', {'game_detail': game_detail, 'velca_stats': velca_stats, 'game_stats': game_stats, 'opponent_stats': opponent_stats})
