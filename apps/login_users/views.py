from urllib.request import urlopen
import json

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.contrib import auth, messages
from .forms import UsuarioForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404  
from django.core.exceptions import ValidationError
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect


class UsuarioCreate(CreateView):
    template_name = 'login_users/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):        
        grupo = get_object_or_404(Group, name='Doadores')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        #self.objects.create(username=self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de Novo Usuário"
        context['Botao'] = "Cadastrar"
        return context

def carrega_cep(request):
    return render(request,'login_users/via_cep.html')

def pesquisa_cep(request):
    if request.method == 'POST':
        try:
            cep = request.POST['cep']
            url = "http://viacep.com.br/ws/"+cep+"/json"
            response = urlopen(url)
            data = json.loads(response.read())
            if data['uf'] == 'PE':
                messages.success(request,'CEP CORRETO')
                return redirect('signup')
                #return JsonResponse(data)
            else:
                messages.error(request,'Desculpe, infelizmente não estamos atendendo sua localidade.')
                return redirect('cep')
                #return JsonResponse(data)
        except:
            messages.error(request,'Verifique o CEP digitado.')
            return redirect('cep')
