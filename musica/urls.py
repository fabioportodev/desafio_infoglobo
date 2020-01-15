from django.urls import path
from musica.views import post_musica, get_all_musicas, put_musica


urlpatterns = [
    path('addMusica/', post_musica),
    path('listarMusicas/', get_all_musicas),
    path('editarMusica/', put_musica),
]
