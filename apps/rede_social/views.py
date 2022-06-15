from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from urllib.request import urlopen
import json

# Create your views here.

def carrega_cep(request):
    return render(request,'rede_social/via_cep.html')

def pesquisa_cep(request):
    if request.method == 'POST':
        cep = request.POST['cep']
        url = "http://viacep.com.br/ws/"+cep+"/json"
        print('chamou pesquisa cep')
        print(cep)
        print(url)
        response = urlopen(url)
        data = json.loads(response.read())
        print(data)
        print(type(data))
        if data['uf'] == 'PE':
            print('CEP CORRETO')
            return JsonResponse(data)
        else:
            print('CEP INCORRETO')
            return JsonResponse(data)
