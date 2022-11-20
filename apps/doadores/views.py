from django.forms import ValidationError
from django.shortcuts import render
from django.shortcuts import get_object_or_404  
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView
from .models import Doacao, Doadores
from doadores.serializers import DoadoresSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

#class Doadores_rest(GroupRequiredMixin, LoginRequiredMixin):
 #   login_url = reverse_lazy('login')
 #   group_required = u"doadores"
 #   model = Doadores
 #   fields = ['nome', 'sobrenome', 'dt_nasc', 'endereco', 'numero', 'complemento', 'celular', 'Intencao']
 
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

class DoadoresList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Doadores
    template_name = 'doadores/listas_doadores.html'

class DoacaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Doadores"
    model = Doacao
    #intencao = 'DT'
    #queryset = Doacao.objects.filter(intencao=intencao)
    #.values_list('intencao')
    template_name = 'doadores/listas_doacao.html'
    #queryset = Doacao.objects.all()

    #def get_queryset(self):
     #   self.object_list = Doadores.objects.filter(username=self.request.user)
      #  return self.object_list

#do = DoacaoList()

## Model registrar

class DoadoresCreate(LoginRequiredMixin,GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Doadores"
    model = Doadores
    fields = ['nome', 'sobrenome', 'dt_nasc', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'celular', 'Intencao']
    template_name = "doadores/formdoadores.html"
    sucess_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Doadores, username=self.request.user)
        return self.object

    def form_valid(self, form):
        form.instance.username = self.request.user
        url = super().form_(form)
        return url

class DoacaoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Doacao
    fields = ['intencao','classificacao', 'descricao', 'estado', 'quantidade']
    template_name = "doadores/formdoacao.html"
    sucess_url = reverse_lazy('novadoacao')
    success_message = 'Obrigado(a) pela sua doação, com pequenas ações fazemos a diferença. DEUS te abençõe!!'

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Doacao, username=self.request.user)
        return self.object

    def form_valid(self, form):
        form.instance.username = self.request.user
        url = super().form_valid(form)
        return url 



## Atualizar dados de Colaborador 

class DoadoresUpdate(UpdateView, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u"Doadores"
    model = Doadores
    fields = ['dt_nasc', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'celular']
    template_name = 'doadores/formdoadores.html'
    sucess_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Doadores, username=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de Novo Colabordor"
        context['Botao'] = "Atualizar"

        return context

class AtualizacaoDoadorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Doadores
    fields = ['dt_nasc', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'celular']
    template_name = 'doadores/formdoadores.html'
    success_url = reverse_lazy('home')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Doadores, username=self.request.user)
        return self.object

    def form_valid(self, form):
        form.instance.username = self.request.user
        url = super().form_valid(form)
        return url 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de Novo Colabordor"
        context['Botao'] = "Atualizar"

        return context