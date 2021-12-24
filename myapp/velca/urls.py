from django.urls import path
from . import views

app_name = 'velca'

urlpatterns = [
  path('', views.index, name='index'),
  path('game_data/', views.GameDataView.as_view(), name='game_data'),
  path('game_detail/<int:game_id>/', views.game_detail, name='game_detail'),
  path('club_list/', views.ClubDataView.as_view(), name='club_list'),
  path('club_detail/<int:pk>/', views.ClubDetail.as_view(), name='club_detail'),
]
