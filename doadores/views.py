from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from doadores.models import Doadores
from doadores.serializers import DoadoresSerializer

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


#class Doadores_rest(GroupRequiredMixin, LoginRequiredMixin):
 #   login_url = reverse_lazy('login')
 #   group_required = u"doadores"
 #   model = Doadores
 #   fields = ['nome', 'sobrenome', 'dt_nasc', 'endereco', 'numero', 'complemento', 'celular', 'Intenção']
 
 #   template_name = 'doadores/form.html'
    
@csrf_exempt

def doadoresApi(request, id=0):
    if request.method=="GET":
        doadores = Doadores.objects.all()
        doadores_serializer = DoadoresSerializer(doadores, many=True)
        return JsonResponse(doadores_serializer.data, safe=False)
    elif request.method=="POST":
        doador_data = JSONParser().parse(request)
        doador_serializer = DoadoresSerializer(data=doador_data)
        if doador_serializer.is_valid():
            doador_serializer.save()
            return JsonResponse("Cadastro realizado com sucesso!!!", safe=False)
        return JsonResponse("Ocorreu um erro durante a gravação dos dados, tente novamente", safe=False)

    elif request.method=="PUT":
        doador_data = JSONParser().parse(request)
        doador = Doadores.objects.get(id_doadores=doador_data['id_doadores'])
        doador_serializer = DoadoresSerializer(doador, data=doador_data)
        if doador_serializer.is_valid():
            doador_serializer.save()
            return JsonResponse("Atualização realizada com sucesso!!!!!!", safe=False)
        return JsonResponse("Falha na atualização do cadastro", safe=False)

    elif request.method=="DELETE":
        doador = Doadores.objects.get(id_doadores=id)
        doador.delete()
        return JsonResponse("Cadastro cancelado com Sucesso!!!", safe=False)