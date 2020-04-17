from django.shortcuts import render
from django.http import HttpResponse
from .solver.grid import grid
from .solver.solver import solver
import pandas as pd


initial_grid = grid()
solved_grid = solver(initial_grid)

# Create your views here.

# def index(response):
# 	return render(response, "main/base.html", {})


def home(response):
    x = ''
    return render(response, 'main/home.html', {"grid": initial_grid})

def new_game(response):
    return render(response, 'main/new_game.html', {"grid": initial_grid})

def previous_games(response):
    return render(response, 'main/previous_games.html', {"grid": solved_grid})

def profile(response):
    return render(response, 'main/profile.html', {})