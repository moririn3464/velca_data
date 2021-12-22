from typing import List
from django.db import models
from django.db.models import query
from django.http import request
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Player_personal, Club, Stats, Game

def index(request):
  return render(request, 'velca/index.html')

class GameDataView(ListView):
  template_name = 'velca/game_data.html'
  model = Game

def game_detail(request, game_id):
  game_detail = Game.objects.get(id=game_id)
  game_stats = game_detail.game_stats.all()
  velca_stats = game_detail.game_stats.filter(player__players_team=1)
  opponent_stats = game_detail.game_stats.filter(player__players_team=2)

  return render(
    request, 
    'velca/game_detail.html', 
    {
      'game_detail': game_detail, 
      'velca_stats': velca_stats, 
      'game_stats': game_stats, 
      'opponent_stats': opponent_stats
    })


class ClubDetail(DetailView):
  model = Club
  template_name = "velca/club_detail.html"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      club_player_list = Player_personal.objects.filter(players_team_id=self.kwargs['pk'])  # pkを指定してデータを絞り込む
      context['club_player_list'] = club_player_list
      return context
