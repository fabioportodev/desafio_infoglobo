from core.models import Artista, GeneroMusical, Musica, Album
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q
import json


@csrf_exempt
def listar_artistas(request):

    if request.method == 'GET':
        name = request.GET['value']
        page = request.GET['page']
        size = request.GET['size']
        artistas = Artista.objects.filter(nome_artista__contains=name)
        result = []
        paginator = Paginator(artistas, size).get_page(page)
        pag_list = list(paginator)
        for a in pag_list:

            result.append({'id': a.id,
                           'id_artista': a.id_artista,
                           'id_amg': a.id_amg,
                           'tipo_artista': a.tipo_artista,
                           'nome_artista': a.nome_artista,
                           'url_artista': a.url_artista,
                           'genero_musical': a.genero_musical.nome_genero})



        result_json = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result_json, content_type='application/json')
    return HttpResponse(json.dumps({
        "Error": "Metodo {} não suportado.".format(request.method)
    }, ensure_ascii=False), status=400, content_type='application/json')


@csrf_exempt
def listar_artista_por_id(request, id):

    if request.method == 'GET':

        a = Artista.objects.get(pk=id)

        result = {'id': a.id,
                  'id_artista': a.id_artista,
                  'id_amg': a.id_amg,
                  'tipo_artista': a.tipo_artista,
                  'nome_artista': a.nome_artista,
                  'url_artista': a.url_artista,
                  'genero_musical': a.genero_musical.nome_genero}



        result_json = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result_json, content_type='application/json')
    return HttpResponse(json.dumps({
        "Error": "Metodo {} não suportado.".format(request.method)
    }, ensure_ascii=False), status=400, content_type='application/json')


@csrf_exempt
def adicionar_artista(request):
    response = {}

    if request.method == 'POST':
        if request.body is None or request.body == "":
            return response

        body = json.loads(request.body)

        fields_to_validate = ["id_artista",
					          "id_amg",
					          "tipo_artista",
					          "nome_artista",
					          "url_artista",
					          "genero_musical"]



        for field in fields_to_validate:
            if field not in body:
                return HttpResponse(json.dumps({
                    "Error": "O atributo {} não está no Body da requisição.".format(field)
                }, ensure_ascii=False), status=400, content_type='application/json')

        try:

            genero = GeneroMusical.objects.get(pk=body['genero_musical'])

            artista = Artista.objects.create(id_artista=body['id_artista'],
                                            id_amg=body['id_amg'],
                                            tipo_artista=body['tipo_artista'],
                                            nome_artista=body['nome_artista'],
                                            url_artista=body['url_artista'],
                                            genero_musical=genero)
            artista.save(force_insert=False)


            return HttpResponse(json.dumps({
                "Success": "As informações foram adicionadas ao banco."
            }, ensure_ascii=False), status=201, content_type='application/json')

        except Exception as e:
            return HttpResponse(json.dumps({
                "Error": "O tipo de dado informado está incorreto"
            }, ensure_ascii=False), status=404, content_type='application/json')


@csrf_exempt
def editar_artista(request, id):
    response = {}

    if request.method == 'PUT':
        if request.body is None or request.body == "":
            return response

        body = json.loads(request.body)

        fields_to_validate = ["id_artista",
					          "id_amg",
					          "tipo_artista",
					          "nome_artista",
					          "url_artista",
					          "genero_musical"]

        for field in fields_to_validate:
            if field not in body:
                return HttpResponse(json.dumps({
                    "Error": "O atributo {} não está no Body da requisição.".format(field)
                }, ensure_ascii=False), status=400, content_type='application/json')

        try:
            artista = Artista.objects.filter(pk=id).values()

            if artista[0]['nome_artista'] != '':
                artista.update(id_artista=body['id_artista'],
                               id_amg=body['id_amg'],
                               tipo_artista=body['tipo_artista'],
                               nome_artista=body['nome_artista'],
                               url_artista=body['url_artista'],
                               genero_musical=body['genero_musical'])

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
def remover_artista(request, id):

    if request.method == 'DELETE':
        try:
            artista = Artista.objects.get(pk=id).delete()

            return HttpResponse(json.dumps({
                "Success": "Removido com sucesso."
            }, ensure_ascii=False), status=200, content_type='application/json')

        except Exception as e:
            return HttpResponse(json.dumps({
                "Error": "O id {} não existe.".format(id)
            }, ensure_ascii=False), status=404, content_type='application/json')


@csrf_exempt
def musicas_do_artista(request, id):

    if request.method == 'GET':
        try:
            page = request.GET['page']
            size = request.GET['size']
            musicas = Musica.objects.filter(artista=id)
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


@csrf_exempt
def albuns_do_artista(request, id):

    if request.method == 'GET':
        try:
            page = request.GET['page']
            size = request.GET['size']
            musicas = Album.objects.filter(artista=id)
            result = []
            paginator = Paginator(musicas, size).get_page(page)
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


        except Exception as e:
            return HttpResponse(json.dumps({
                "Error": "O id {} não existe.".format(id)
            }, ensure_ascii=False), status=404, content_type='application/json')