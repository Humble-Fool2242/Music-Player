from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from musicbeats.models import Song, ListenLater, History
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    trending_songs = Song.objects.all
    context = {'songs': trending_songs}
    return render(request, 'index.html', context)


def songs(request):
    if request.user.is_authenticated:
        all_songs = Song.objects.all
        context = {'songs': all_songs}
        return render(request, 'songs.html', context)
    else:
        return render(request, 'signup.html')


def song(request, id):
    if request.user.is_authenticated:
        message = ""
        search_song = Song.objects.get(song_id=id)
        context = {'song': search_song}
        if request.method == 'POST':
            user = request.user
            saved_or_not = ListenLater.objects.filter(user=user, audio_id=id).exists()

            if not saved_or_not:
                listenlater = ListenLater(user=user, audio_id=id)
                listenlater.save()
                message = "Your song is saved."
            else:
                message = "Your song is already saved."
            context['message'] = message
            song = Song.objects.filter(song_id=id).first()
            return render(request, 'song.html', {'song': song, 'context': context})

        else:
            user = request.user
            music_id = str(id)
            history = History(user=user, audio_id=music_id)
            history.save()
            context['message'] = message
            song = Song.objects.filter(song_id=id).first()
            return render(request, 'song.html', {'song': song, 'context': context})

    else:
        return render(request, 'signup.html')


def signup(request):
    print("hi")
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            return redirect(request, '/musicbeats/signup')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        user = authenticate(username=username, password=pass1)
        login(request, user)
        return redirect('/')
    print("ok")
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'signin.html')


def listenlater(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            song_id = request.POST['song_id']
            remove_item = ListenLater.objects.filter(audio_id=song_id)
            remove_item.delete()
            return redirect("/musicbeats/listenlater")

        else:
            user = request.user
            saved_songs_id = []
            saved_songs = []
            all_songs = Song.objects.all()
            all_saved_songs = ListenLater.objects.all().filter(user=user)
            for saved_song in all_saved_songs:
                saved_songs_id.append(saved_song.audio_id)

            for song in all_songs:
                cnt = saved_songs_id.count(str(song.song_id))
                if cnt > 0:
                    saved_songs.append(song)

            context = {'saved_songs': saved_songs}
            return render(request, 'listenlater.html', context)
    else:
        return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return redirect('/musicbeats')


def history(request):

    history_songs_id = []
    history_songs = []
    all_songs = Song.objects.all()
    all_hist_songs = History.objects.all().filter(user=request.user)
    for history_song in all_hist_songs:
        history_songs_id.append(history_song.audio_id)

    for song in all_songs:
        cnt = history_songs_id.count(str(song.song_id))
        if cnt > 0:
            history_songs.append(song)

    return render(request, 'history.html', {'songs': history_songs})
