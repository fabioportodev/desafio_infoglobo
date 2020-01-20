from django.urls import path
from album.views import adicionar_album, \
    listar_albuns, \
    listar_album_por_id, \
    editar_album, \
    remover_album, \
    musicas_do_album


urlpatterns = [
    path('adicionarAlbum/', adicionar_album),
    path('listarAlbum/', listar_albuns),
    path('listarAlbum/<int:id>/', listar_album_por_id),
    path('editarAlbum/<int:id>/', editar_album),
    path('removerAlbum/<int:id>/', remover_album),
    path('musicasAlbum/<int:id>/', musicas_do_album),
]
