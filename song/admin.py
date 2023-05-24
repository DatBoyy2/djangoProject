from django.contrib import admin
from .models import Author,Song,Album
# Register your models here.
admin.site.register(Author)
admin.site.register(Song)
admin.site.register(Album)