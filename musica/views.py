from core.models import Album, GeneroMusical, Artista, Musica
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def post_musica(request):
    response = {}

    if request.method == 'POST':
        if request.body is None or request.body == "":
            return response

        body = json.loads(request.body)

        fields_to_validate = ["id_musica",
					          "nome_musica",
					          "url_musica",
                              "url_preview",
                              "url_art_trinta",
                              "url_art_sessenta",
                              "url_art_cem",
                              "preco_musica",
                              "lancamento",
                              "classificacao",
                              "posicao_faixa",
                              "tempo_musica",
                              "pais",
                              "moeda",
                              "stream",
					          "genero_musical",
                              "artista",
                              "album"]


        for field in fields_to_validate:
            if field not in body:
                return HttpResponse(json.dumps({
                    "Error": "O atributo {} não está no Body da requisição.".format(field)
                }, ensure_ascii=False), status=400, content_type='application/json')

        genero = GeneroMusical.objects.get(pk=body['genero_musical'])
        artista = Artista.objects.get(pk=body['artista'])
        album = Album.objects.get(pk=body['album'])

        musica = Musica.objects.create(id_musica=body['id_musica'],
                                       nome_musica=body['nome_musica'],
                                       url_musica=body['url_musica'],
                                       url_preview=body['url_preview'],
                                       url_art_trinta=body['url_art_trinta'],
                                       url_art_sessenta=body['url_art_sessenta'],
                                       url_art_cem=body['url_art_cem'],
                                       preco_musica=body['preco_musica'],
                                       lancamento=body['lancamento'],
                                       classificacao=body['classificacao'],
                                       faixa_n=body['posicao_faixa'],
                                       tempo_musica=body['tempo_musica'],
                                       pais=body['pais'],
                                       moeda=body['moeda'],
                                       stream=body['stream'],
                                       genero_musical=genero,
                                       artista=artista,
                                       album=album
                                       )
        musica.save(force_insert=False)


        return HttpResponse(json.dumps({
            "Success": "As informações foram salvas no banco."
        }, ensure_ascii=False), status=201, content_type='application/json')