from django.contrib import admin
from .models import Song, ListenLater, History

# Register your models here.
admin.site.register(Song)
admin.site.register(ListenLater)
admin.site.register(History)