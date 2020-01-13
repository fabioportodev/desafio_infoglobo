from django.urls import path
from genero_musical.views import post_genero_musical


urlpatterns = [
    path('AddGeneroMusical/', post_genero_musical),
]
