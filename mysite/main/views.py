from django.shortcuts import render
from django.http import HttpResponse
from .solver.grid import grid

x = grid()
# Create your views here.

def index(response):
	return render(response, "main/base.html", {})

def home(response):
    return render(response, 'main/home.html', {"grid": grid})
