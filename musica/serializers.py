from rest_framework.serializers import ModelSerializer
from core.models import Musica, GeneroMusical


class MusicaSerializer(ModelSerializer):

	class Meta:
		model = Musica
		fields = ('__all__')


class GeneroMusicalSerializer(ModelSerializer):

	class Meta:
		model = GeneroMusical
		fields = ('__all__')