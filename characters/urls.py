# characters/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('create_pathfinder/', views.create_pathfinder, name='create_pathfinder'),
]