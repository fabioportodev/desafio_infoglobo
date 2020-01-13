from django.urls import path
from musica.views import post_musica


urlpatterns = [
    path('AddMusica/', post_musica),
]
