from django.urls import path
from . import views

urlpatterns = [
    path('matches/', views.match_list, name='match_list'),
    path('add_match/', views.add_match, name='add_match'),
    path('team/<int:team_id>/', views.team_info, name='team_info'),
]