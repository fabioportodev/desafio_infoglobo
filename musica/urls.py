from django.urls import path
from musica.views import adicionar_musica, \
    listar_musicas, \
    editar_musica, \
    listar_musica_por_id, \
    remover_musica


urlpatterns = [
    path('addMusica/', adicionar_musica),
    path('listarMusicas/', listar_musicas),
    path('listarMusicas/<int:id>/', listar_musica_por_id),
    path('editarMusica/<int:id>/', editar_musica),
    path('removerMusica/<int:id>/', remover_musica),

]
