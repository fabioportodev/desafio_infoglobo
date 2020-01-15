from django.urls import path
from genero_musical.views import post_genero_musical, get_all_generos


urlpatterns = [
    path('AddGenero/', post_genero_musical),
    path('listarGeneros/', get_all_generos),

]
