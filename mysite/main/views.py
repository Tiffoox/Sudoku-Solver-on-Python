from django.shortcuts import render
from django.http import HttpResponse
from .solver.grid import grid
from .solver.solver import solver
import pandas as pd

initial_grid = grid()
solved_grid = solver(initial_grid)

# Create your views here.
def new_game(response):
    return render(response, 'main/new_game.html', {"grid": initial_grid})
# def index(response):
# 	return render(response, "main/base.html", {})

def home(response):
    return render(response, 'main/home.html', {"grid": initial_grid})

def solved(response):
    return render(response, 'main/solved.html', {"grid": solved_grid})
