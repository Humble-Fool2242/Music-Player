from django.shortcuts import render, redirect
from musicbeats.models import Song


def index(request):
    trending_songs = Song.objects.all
    context = {'songs': trending_songs}
    return render(request, 'index.html', context)


def songs(request):
    all_songs = Song.objects.all
    context = {'songs': all_songs}
    return render(request, 'songs.html', context)


def song(request, song_id):
    search_song = Song.objects.get(song_id=song_id)
    context = {'song': search_song}
    return render(request, 'song.html', context)
