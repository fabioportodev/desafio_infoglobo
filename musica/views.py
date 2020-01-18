from core.models import Album, GeneroMusical, Artista, Musica
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def get_all_musicas(request):

    if request.method == 'GET':

        musicas = Musica.objects.all()
        result = []
        for m in musicas:

            result.append({'id': m.id,
                        'nome_musica': m.nome_musica,
                        'url_musica': m.url_musica,
                        'url_preview': m.url_preview,
                        'url_art_trinta': m.url_art_trinta,
                        'url_art_sessenta': m.url_art_sessenta,
                        'url_art_cem': m.url_art_cem,
                        'preco_musica': str(m.preco_musica),
                        'lancamento': m.lancamento,
                        'classificacao': m.classificacao,
                        'posicao_faixa': m.faixa_n,
                        'tempo_musica': m.tempo_musica,
                        'pais': m.pais,
                        'moeda': str(m.moeda),
                        'stream': str(m.stream),
                        'genero_musical': m.genero_musical.nome_genero,
                        'artista': m.artista.nome_artista,
                        'album': m.album.nome_album})



        result_json = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result_json, content_type='application/json')
    return HttpResponse(json.dumps({
        "Error": "Metodo {} não suportado.".format(request.method)
    }, ensure_ascii=False), status=400, content_type='application/json')



@csrf_exempt
def post_musica(request):
    response = {}

    if request.method == 'POST':
        if request.body is None or request.body == "":
            return response

        body = json.loads(request.body)

        fields_to_validate = ["id",
                              "id_musica",
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



@csrf_exempt
def put_musica(request):
    pass
    '''
    response = {}

    if request.method == 'PUT':
        if request.body is None or request.body == "":
            return response

        body = json.loads(request.body)

        fields_to_validate = ["id",
                              "id_musica",
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



        musica = Musica.objects.filter(pk=body['id']).update(
                                       id_musica=body['id_musica'],
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
                                       genero_musical=body['genero_musical'],
                                       artista=body['artista'],
                                       album=body['album']
                                       )
        
        musica = Musica.objects.filter(pk=body['id']).update(
            id_musica=True,
            nome_musica=True,
            url_musica=True,
            url_preview=True,
            url_art_trinta=True,
            url_art_sessenta=True,
            url_art_cem=True,
            preco_musica=True,
            lancamento=True,
            classificacao=True,
            faixa_n=True,
            tempo_musica=True,
            pais=True,
            moeda=True,
            stream=True,
            genero_musical=True,
            artista=True,
            album=True
        )
        
        musica.save()

        return HttpResponse(json.dumps({
            "Success": "As informações foram salvas no banco."
        }, ensure_ascii=False), status=201, content_type='application/json')
    
    '''