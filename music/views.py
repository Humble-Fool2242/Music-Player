from django.shortcuts import render, redirect
from musicbeats.models import Song


def index(request):
    songs = Song.objects.all
    context = {'songs': songs}
    return render(request, 'index.html', context)
