from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('home/', views.home, name='home'),
    path('previous_games/', views.previous_games, name = 'solved'),
    path('new_game/', views.new_game, name = 'new game')
]
