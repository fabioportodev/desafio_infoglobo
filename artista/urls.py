from django.urls import path
from artista.views import adicionar_artista, \
    listar_artistas, \
    listar_artista_por_id, \
    editar_artista, \
    remover_artista, \
    musicas_do_artista, \
    albuns_do_artista


urlpatterns = [
    path('adicionarArtista/', adicionar_artista),
    path('listarArtista/', listar_artistas),
    path('listarArtista/<int:id>/', listar_artista_por_id),
    path('editarArtista/<int:id>/', editar_artista),
    path('removerArtista/<int:id>/', remover_artista),
    path('musicasArtista/<int:id>/', musicas_do_artista),
    path('albunsArtista/<int:id>/', albuns_do_artista),
]
