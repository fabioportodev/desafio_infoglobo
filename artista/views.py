from core.models import Artista, GeneroMusical
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def post_artista(request):
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




