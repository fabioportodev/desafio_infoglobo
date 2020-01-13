from django.db import models


class GeneroMusical(models.Model):
	nome_genero = models.CharField(max_length=50)

	def __str__(self):
		return self.nome_genero


class Artista(models.Model):
	id_artista = models.IntegerField()
	id_amg = models.IntegerField()
	tipo_artista = models.CharField(max_length=30)
	nome_artista = models.CharField(max_length=100)
	url_artista = models.CharField(max_length=150)

	genero_musical = models.ForeignKey('GeneroMusical', on_delete=models.CASCADE)

	def __str__(self):
		return self.nome_artista


class Album(models.Model):
	id_album = models.IntegerField(null=False)
	nome_album = models.CharField(max_length=100)
	tipo_album = models.CharField(max_length=50)
	url_album = models.CharField(max_length=150)
	url_art_sessenta = models.CharField(max_length=300)
	url_art_cem = models.CharField(max_length=300)
	preco_album = models.DecimalField(max_digits=5, decimal_places=2)
	classificacao = models.CharField(max_length=50)
	n_faixas = models.IntegerField()
	copyright = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	moeda = models.CharField(max_length=20)
	lancamento = models.CharField(max_length=20)

	artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
	genero_musical = models.ForeignKey('GeneroMusical', on_delete=models.CASCADE)



	def __str__(self):
		return self.nome_album


class Musica(models.Model):

	id_musica = models.IntegerField(null=False)
	nome_musica = models.CharField(max_length=50)
	url_musica = models.CharField(max_length=150)
	url_preview = models.CharField(max_length=150)
	url_art_trinta = models.CharField(max_length=150)
	url_art_sessenta = models.CharField(max_length=150)
	url_art_cem = models.CharField(max_length=150)
	preco_musica = models.DecimalField(max_digits=5, decimal_places=2)
	lancamento = models.CharField(max_length=20)
	classificacao = models.CharField(max_length=50)
	faixa_n = models.IntegerField()
	tempo_musica = models.IntegerField()
	pais = models.CharField(max_length=50)
	moeda = models.CharField(max_length=20)
	stream = models.CharField(max_length=10)

	artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
	album = models.ForeignKey('Album', on_delete=models.CASCADE)
	genero_musical = models.ForeignKey('GeneroMusical', on_delete=models.CASCADE)


	def __str__(self):
		return self.nome_musica
