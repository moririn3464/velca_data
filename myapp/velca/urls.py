from django.urls import path
from . import views

app_name = 'velca'

urlpatterns = [
  path('', views.index, name='index'),
  path('player_list', views.player_list, name='player_list'),
  # path('spnav', views.spnav, name='spnav')
]
