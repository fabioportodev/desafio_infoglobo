from django.contrib import admin
from django.urls import path, include
import artista.urls, album.urls, genero_musical.urls, musica.urls


urlpatterns = [
    path('artista/',include(artista.urls)),
    path('album/',include(album.urls)),
    path('genero/',include(genero_musical.urls)),
    path('musica/',include(musica.urls)),
    path('admin/', admin.site.urls),

]
