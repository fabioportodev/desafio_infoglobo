from core.models import Album, GeneroMusical, Artista
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def post_album(request):
    response = {}

    if request.method == 'POST':
        if request.body is None or request.body == "":
            return response

        body = json.loads(request.body)

        fields_to_validate = ["id_album",
					          "tipo_album",
					          "nome_album",
					          "url_album",
                              "url_art_sessenta",
                              "url_art_cem",
                              "preco_album",
                              "classificacao",
                              "n_faixas",
                              "copyright",
                              "pais",
                              "moeda",
                              "lancamento",
					          "genero_musical",
                              "artista"]


        for field in fields_to_validate:
            if field not in body:
                return HttpResponse(json.dumps({
                    "Error": "O atributo {} não está no Body da requisição.".format(field)
                }, ensure_ascii=False), status=400, content_type='application/json')

        genero = GeneroMusical.objects.get(pk=body['genero_musical'])
        artista = Artista.objects.get(pk=body['artista'])

        album = Album.objects.create(id_album=body['id_album'],
                                     tipo_album=body['tipo_album'],
                                     nome_album=body['nome_album'],
                                     url_album=body['url_album'],
                                     url_art_sessenta=body['url_art_sessenta'],
                                     url_art_cem=body['url_art_cem'],
                                     preco_album=body['preco_album'],
                                     classificacao=body['classificacao'],
                                     n_faixas=body['n_faixas'],
                                     copyright=body['copyright'],
                                     pais=body['pais'],
                                     moeda=body['moeda'],
                                     lancamento=body['lancamento'],
                                     genero_musical=genero,
                                     artista=artista)
        album.save(force_insert=False)


        return HttpResponse(json.dumps({
            "Success": "As informações foram salvas no banco."
        }, ensure_ascii=False), status=201, content_type='application/json')