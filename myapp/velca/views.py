from django.shortcuts import render
from .models import Player

def index(request):
  return render(request, 'velca/index.html')

def player_list(request):
  players_pdata = Player.objects.all()
  return render(request, 'velca/player_list.html', {'players_pdata': players_pdata})
