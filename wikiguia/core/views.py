from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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


def guides(request):
    games = Game.objects.filter(is_visible=True)
    return render(request, 'core/guides.html',{
        'games' : games,
    })

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


def admin_logout(request):
    logout(request)
    messages.success(request,"Logout correcto")

    return redirect('core:index')