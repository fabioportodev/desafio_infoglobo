from django.urls import path
from album.views import post_album


urlpatterns = [
    path('AddAlbum/', post_album),
]
