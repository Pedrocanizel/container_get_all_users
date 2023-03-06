from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .postgres_conn import get_lines

'''
Para fazer uma consulta em todos os itens da tabela,
enviar uma requisição "GET" vazia
'''

@api_view(['GET'])
def select_all(request):

    try:
        if len(request.data) == 0:
            retorno = get_lines()
            return JsonResponse(retorno, status=201, safe=False)
            
    except Exception as ex:
        response = {
            "error": str(ex.args[0])
        }
        return JsonResponse(response, status=400)






