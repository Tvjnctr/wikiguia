from django.shortcuts import render
from games.models import Game
# Create your views here.

def index(request):
    games = Game.objects.all
    return render(request, 'core/index.html', {
        'games' : games, 
    })


def contact(request):
    return render(request, 'core/contact.html')
