from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .maker_and_solver.grid import grid
from .maker_and_solver.solver import solver
import pandas as pd
import random
import json


def home(response):
    x = ''
    return render(response, 'main/home.html', {})

def new_game(response):

    return render(response, 'main/new_game.html', {})


def gameplay(response):
    initial_grid = grid()
    json_data = json.loads(json.dumps(initial_grid.tolist()))
    return render(response, 'main/gameplay.html', {"grid": json_data})

def solved_grid(response):
    initial_grid = grid()
    solved_grid = solver(initial_grid)
    json_data = json.loads(json.dumps(solved_grid.tolist()))
    return render(response, 'main/gameplay.html', {"grid": json_data})


def previous_games(response):
    return render(response, 'main/previous_games.html', {})

def profile(response):
    return render(response, 'main/profile.html', {})