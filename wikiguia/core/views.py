from django.shortcuts import render
from game.models import Game
# Create your views here.

def index(request):  
    games = Game.objects.filter(is_visible=True)  
    return render(request, 'core/index.html',{
        'games' : games,
    })

def contact(request):
    return render(request, 'core/contact.html')
