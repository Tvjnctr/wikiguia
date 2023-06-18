from django.shortcuts import render, redirect
from game.models import Game
from . forms import SignupForm
# Create your views here.

def index(request):  
    games = Game.objects.filter(is_visible=True)  
    return render(request, 'core/index.html',{
        'games' : games,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    else:
        form = SignupForm()
    
    

    return render(request, 'core/signup.html',{
        'form':form
    })
