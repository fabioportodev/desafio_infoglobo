from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from core.models import Artista, GeneroMusical


class ArtistaSerializer(HyperlinkedModelSerializer):

	class Meta:
		model = Artista
		fields = ('id_artista',
		          'id_amg',
		          'tipo_artista',
		          'nome_artista',
		          'url_artista',
		          'genero_musical')