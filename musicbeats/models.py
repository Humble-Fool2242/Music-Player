from django.db import models


# Create your models here

class Song(models.Model):
    song_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/documents')
    song = models.FileField(upload_to='media/documents')

    def __str__(self):
        return self.name
