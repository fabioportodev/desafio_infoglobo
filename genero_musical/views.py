from core.models import GeneroMusical
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import HttpResponse
import json


@csrf_exempt
def listar_generos(request):

    if request.method == 'GET':
        name = request.GET['value']
        page = request.GET['page']
        size = request.GET['size']
        genero = GeneroMusical.objects.filter(nome_genero__contains=name)
        result = []
        paginator = Paginator(genero, size).get_page(page)
        pag_list = list(paginator)
        for g in pag_list:
            result.append({'id': g.id,
                      'genero': g.nome_genero})

        result_json = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result_json, content_type='application/json')
    return HttpResponse(json.dumps({
        "Error": "Metodo {} não suportado.".format(request.method)
    }, ensure_ascii=False), status=400, content_type='application/json')


@csrf_exempt
def listar_genero_por_id(request, id):

    if request.method == 'GET':
        g = GeneroMusical.objects.get(pk=id)

        result = {'id': id,
                  'genero': g.nome_genero}

        result_json = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result_json, content_type='application/json')
    return HttpResponse(json.dumps({
        "Error": "Metodo {} não suportado.".format(request.method)
    }, ensure_ascii=False), status=400, content_type='application/json')


@csrf_exempt
def adicionar_genero(request):
    response = {}

    if request.method == 'POST':
        if request.body is None or request.body == "":
            return response

        body = json.loads(request.body)

        fields_to_validate = ["nome_genero"]

        for field in fields_to_validate:
            if field not in body:
                return HttpResponse(json.dumps({
                    "Error": "O atributo {} não está no Body da requisição.".format(field)
                }, ensure_ascii=False), status=400, content_type='application/json')


        genero = GeneroMusical.objects.create(nome_genero=body['nome_genero'])
        genero.save(force_insert=False)


        return HttpResponse(json.dumps({
            "Success": "As informações foram adicionadas ao banco."
        }, ensure_ascii=False), status=201, content_type='application/json')


@csrf_exempt
def editar_genero(request, id):
    response = {}

    if request.method == 'PUT':
        if request.body is None or request.body == "":
            return response

        body = json.loads(request.body)

        fields_to_validate = ["nome_genero"]

        for field in fields_to_validate:
            if field not in body:
                return HttpResponse(json.dumps({
                    "Error": "O atributo {} não está no Body da requisição.".format(field)
                }, ensure_ascii=False), status=400, content_type='application/json')

        try:
            genero = GeneroMusical.objects.filter(pk=id).values()

            if genero[0]['nome_genero'] != '':
                genero.update(
                    nome_genero=body['nome_genero']
                )
                return HttpResponse(json.dumps({
                    "Success": "As informações foram salvas no banco."
                }, ensure_ascii=False), status=201, content_type='application/json')

            else:
                return HttpResponse(json.dumps({
                    "Error": "O id {} não existe.".format(id)
                }, ensure_ascii=False), status=404, content_type='application/json')


        except Exception as e:
            return HttpResponse(json.dumps({
                "Error": "O id {} não existe.".format(id)
            }, ensure_ascii=False), status=404, content_type='application/json')



@csrf_exempt
def remover_genero(request, id):

    if request.method == 'DELETE':
        try:
            genero = GeneroMusical.objects.get(pk=id).delete()

            return HttpResponse(json.dumps({
                "Success": "Removido com sucesso."
            }, ensure_ascii=False), status=200, content_type='application/json')

        except Exception as e:
            return HttpResponse(json.dumps({
                "Error": "O id {} não existe.".format(id)
            }, ensure_ascii=False), status=404, content_type='application/json')



