from django.shortcuts import render, get_object_or_404
from .models import Game

def detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    return render(request, 'game/detail.html', {
        'game' : game
    })
