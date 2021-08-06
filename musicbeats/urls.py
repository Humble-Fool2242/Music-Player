from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('songs/', views.songs, name="songs"),
    path('song/<int:id>', views.song, name='song'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('listenlater', views.listenlater, name='listenlater'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('history', views.history, name='history'),

]
