from django.urls import path
from artista.views import post_artista


urlpatterns = [
    path('AddArtistas/', post_artista),
]
