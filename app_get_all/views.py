from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .postgres_conn import get_lines
from django.views.decorators.csrf import csrf_exempt
from . import valida_token as vt 
'''
Para fazer uma consulta em todos os itens da tabela,
enviar uma requisição "GET" vazia
'''
@csrf_exempt
@api_view(['POST'])
def select_all(request):
    
    token = request.headers['Authorization']
    #data = request.data
    email = request.headers['email']
    status = vt.valida_token_navegacao(email, token, 'nav')
    status = status.json()
    if status['FL_STATUS'] == False:
        resposta = {
            "msg": "token expirado",
            "FL_STATUS": False        
            }
        return JsonResponse(resposta, status=400, safe=False)

    try:
        if len(request.data) == 0:
            retorno ={
            "FL_STATUS": True,
            "data": get_lines()
            } 
            return JsonResponse(retorno, status=201, safe=False)
            
    except Exception as ex:
        response = {
            "FL_STATUS": False,
            "error": str(ex.args[0])
        }
        return JsonResponse(response, status=400)






