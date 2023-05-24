from django.db import models

# Create your models here.
class Author(models.Model):

    name = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    photo = models.CharField(max_length=400)
    spotify_link = models.CharField(max_length=200)
    biography = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Song(models.Model):
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    photo = models.CharField(max_length=400)
    spotify = models.CharField(max_length=400, null=True)
    lengths = models.CharField(max_length=40)
    lyrics = models.TextField(max_length=100000)


    def __str__(self):
        return self.song_name

class Album(models.Model):
    album_Name = models.CharField(max_length=40)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    views = models.IntegerField(default=0)
    photo = models.CharField(max_length=200)
    spotify_link = models.CharField(max_length=200)

    def __str__(self):
        return self.album_Name