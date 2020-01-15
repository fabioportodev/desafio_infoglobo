from django.urls import path
from artista.views import post_artista, get_all_artista


urlpatterns = [
    path('addArtistas/', post_artista),
    path('listarArtistas/', get_all_artista),
]
