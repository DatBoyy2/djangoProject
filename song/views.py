from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Author,Song,Album

# Create your views here.
def index(request):
    context = {'contenido': None}
    return render(request,'song/index.html',context)

def songs(request):
    list_of_songs = Song.objects.all()
    context = {'songs': list_of_songs}
    return render(request,'song/songs.html',context)

def author(request):
    list_of_authors = Author.objects.all()
    context = {'authors': list_of_authors,}
    return render(request,'song/author.html',context)

def album(request):
    list_of_albums = Album.objects.all()
    context = {'albums': list_of_albums}
    return render(request,'song/album.html',context)

def album_id(request,album_id):
    try:
        album_info = Album.objects.get(id=album_id)
        for song in album_info.songs.all():
            print(song)

        context = {'album': album_info}
        return render(request, 'song/single_album.html',context)
    except:
        raise Http404("Author not exist")

def author_id(request,author_id):
    try:
        author_info = Author.objects.get(id=author_id)
        context = {'author': author_info}
        return render(request, 'song/author_info.html',context)
    except:
        raise Http404("Author not exist")

def song_id(request,songs_id):
    try:
        song_info = Song.objects.get(id=songs_id)
        context = {'song': song_info}
        return render(request, 'song/song_info.html',context)
    except:
        raise Http404("Author not exist")
