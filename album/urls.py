from django.urls import path
from album.views import post_album, get_all_albuns


urlpatterns = [
    path('addAlbum/', post_album),
    path('listarAlbuns/', get_all_albuns),
]
