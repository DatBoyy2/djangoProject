from django.urls import path
from . import views

app_name = 'song'
urlpatterns=[
    path('',views.index, name='index'),
    path('album/',views.album, name='album'),
    path('<int:album_id>/album/', views.album_id, name='album_info'),
    path('songs/', views.songs, name='songs'),
    path('<int:songs_id>/song/', views.song_id, name='song_info'),
    path('author/', views.author, name='author'),
    path('<int:author_id>/author/', views.author_id, name='author_id'),

]

