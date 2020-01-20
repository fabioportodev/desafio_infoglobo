from django.urls import path
from genero_musical.views import adicionar_genero, \
    listar_generos, \
    listar_genero_por_id, \
    editar_genero, \
    remover_genero


urlpatterns = [
    path('adicionarGenero/', adicionar_genero),
    path('listarGenero/', listar_generos),
    path('listarGenero/<int:id>/', listar_genero_por_id),
    path('editarGenero/<int:id>/', editar_genero),
    path('removerGenero/<int:id>/', remover_genero),
]
