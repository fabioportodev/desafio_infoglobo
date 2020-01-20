from core.models import Album, GeneroMusical, Artista, Musica
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import HttpResponse
import json


@csrf_exempt
def listar_albuns(request):

    if request.method == 'GET':
        name = request.GET['value']
        page = request.GET['page']
        size = request.GET['size']
        albuns = Album.objects.filter(nome_album__contains=name)
        result = []
        paginator = Paginator(albuns, size).get_page(page)
        pag_list = list(paginator)
        for a in pag_list:

            result.append({'id_album': a.id_album,
                            'tipo_album': a.tipo_album,
                            'nome_album': a.nome_album,
                            'url_album': a.url_album,
                            'url_art_sessenta': a.url_art_sessenta,
                            'url_art_cem': a.url_art_cem,
                            'preco_album': str(a.preco_album),
                            'classificacao': a.classificacao,
                            'n_faixas': a.n_faixas,
                            'copyright': a.copyright,
                            'pais': a.pais,
                            'moeda': str(a.moeda),
                            'lancamento': a.lancamento,
                            'genero_musical': a.genero_musical.nome_genero,
                            'artista': a.artista.nome_artista})



        result_json = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result_json, content_type='application/json')
    return HttpResponse(json.dumps({
        "Error": "Metodo {} não suportado.".format(request.method)
    }, ensure_ascii=False), status=400, content_type='application/json')


@csrf_exempt
def listar_album_por_id(request, id):

    if request.method == 'GET':
        a = Album.objects.get(pk=id)

        result = {'id_album': a.id_album,
                       'tipo_album': a.tipo_album,
                       'nome_album': a.nome_album,
                       'url_album': a.url_album,
                       'url_art_sessenta': a.url_art_sessenta,
                       'url_art_cem': a.url_art_cem,
                       'preco_album': str(a.preco_album),
                       'classificacao': a.classificacao,
                       'n_faixas': a.n_faixas,
                       'copyright': a.copyright,
                       'pais': a.pais,
                       'moeda': str(a.moeda),
                       'lancamento': a.lancamento,
                       'genero_musical': a.genero_musical.nome_genero,
                       'artista': a.artista.nome_artista}

        result_json = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result_json, content_type='application/json')

    return HttpResponse(json.dumps({
        "Error": "Metodo {} não suportado.".format(request.method)
    }, ensure_ascii=False), status=400, content_type='application/json')


@csrf_exempt
def adicionar_album(request):
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

        genero = GeneroMusical.objects.get(nome_genero=body['genero_musical'])
        artista = Artista.objects.get(nome_artista=body['artista'])

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


@csrf_exempt
def editar_album(request, id):
    response = {}

    if request.method == 'PUT':
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

        try:
            genero = GeneroMusical.objects.get(nome_genero=body['genero_musical'])
            artista = Artista.objects.get(nome_artista=body['artista'])
            album = Album.objects.filter(pk=id).values()

            if album[0]['nome_album'] != '':
                album.update(id_album=body['id_album'],
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
                                     genero_musical=genero.id,
                                     artista=artista.id)

                return HttpResponse(json.dumps({
                    "Success": "As informações foram salvas no banco."
                }, ensure_ascii=False), status=201, content_type='application/json')

            else:
                return HttpResponse(json.dumps({
                    "Error": "O id {} não existe.".format(id)
                }, ensure_ascii=False), status=404, content_type='application/json')


        except Exception as e:
            return HttpResponse(json.dumps({
                "Error": "O tipo de dado informado está incorreto"
            }, ensure_ascii=False), status=404, content_type='application/json')


@csrf_exempt
def remover_album(request, id):

    if request.method == 'DELETE':
        try:
            album = Album.objects.get(pk=id).delete()

            return HttpResponse(json.dumps({
                "Success": "Removido com sucesso."
            }, ensure_ascii=False), status=200, content_type='application/json')

        except Exception as e:
            return HttpResponse(json.dumps({
                "Error": "O id {} não existe.".format(id)
            }, ensure_ascii=False), status=404, content_type='application/json')


@csrf_exempt
def musicas_do_album(request, id):

    if request.method == 'GET':
        try:
            page = request.GET['page']
            size = request.GET['size']
            musicas = Musica.objects.filter(album=id)
            result = []
            paginator = Paginator(musicas, size).get_page(page)
            pag_list = list(paginator)

            for m in pag_list:
                result.append({'nome_musica': m.nome_musica,
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

        except Exception as e:
            return HttpResponse(json.dumps({
                "Error": "O id {} não existe.".format(id)
            }, ensure_ascii=False), status=404, content_type='application/json')