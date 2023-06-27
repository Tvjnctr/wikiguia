from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from game.models import Game
# Create your views here.


@login_required
def index(request):
    games = Game.objects.all()  

    return render(request, 'dashboard/index.html',{
        'games' : games,
    })    

