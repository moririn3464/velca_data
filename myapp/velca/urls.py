from django.urls import path
from . import views

app_name = 'velca'

urlpatterns = [
  path('', views.index, name='index'),
  path('player_list/', views.PlayerListView.as_view(), name='player_list'),
  path('game_data/', views.GameDataView.as_view(), name='game_data'),
  path('game_detail/<int:game_id>/', views.game_detail, name='game_detail'),
]
