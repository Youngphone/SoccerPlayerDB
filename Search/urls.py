from django.urls import path
from . import views

urlpatterns = [
    path('searchplayers', views.player_search_view),
    path('searchteams', views.team_search_view),
]
