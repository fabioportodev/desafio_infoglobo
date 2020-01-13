from core.models import GeneroMusical
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
def post_genero_musical(request):
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




