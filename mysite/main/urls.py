from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('home/', views.home, name='home'),
    path('solved/', views.solved, name = 'solved'),
    path('new_game/', views.new_game, name = 'new game')
]