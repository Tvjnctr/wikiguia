from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game
from .forms import NewItemForm

def detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    return render(request, 'game/detail.html', {
        'game' : game
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            game = form.save(commit=False)
            game.save()

            return redirect('game:detail', pk=game.id)

    else:
        form = NewItemForm()

    return render(request, 'game/form.html', {
        'form':form
    })
