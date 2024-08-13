# characters/views.py

from django.shortcuts import render, redirect
from .models import Character


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'characters/character_list.html', {'characters': characters})


def create_pathfinder(request):
    if request.method == "POST":
        char_name = request.POST.get('char_name')
        player = request.POST.get('player')
        race = request.POST.get('race')
        alignment = request.POST.get('alignment')

        Character.objects.create(name=char_name, player=player, race=race, alignment=alignment)

        return redirect('/')

    return render(request, 'characters/create_pathfinder.html')
