from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .solver.grid import grid
from .solver.solver import solver
import pandas as pd
import random
import json


def home(response):
    x = ''
    return render(response, 'main/home.html', {})

def new_game(response):

    return render(response, 'main/new_game.html', {})

def index(response):
    initial_grid = grid()
    json_data = json.loads(json.dumps(initial_grid.tolist()))
    return render(response, 'main/gameplay.html', {"grid": json_data})

def previous_games(response):
    return render(response, 'main/previous_games.html', {})

def profile(response):
    return render(response, 'main/profile.html', {})