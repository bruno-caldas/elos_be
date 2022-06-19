from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404  
from django.core.exceptions import ValidationError
from django.http import HttpRequest, JsonResponse



from urllib.request import urlopen
import json

# Create your views here.

# def carrega_login(request):
  #  return render(request, "login_users/login.html")


class UsuarioCreate(CreateView):
    template_name = 'login_users/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('abrigo')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='Doadores')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        # self.objects.create(username=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de Novo Usuário"
        context['Botao'] = "Cadastrar"
        return context

# class Pesquisa(BaseCreateView):
  #template_name = 'login_users/via_cep.html'
  #success_url = reverse_lazy('abrigo')

  #def pesquisa_cep(request):
   # if request.method == 'POST':
    #  cep = request.POST['cep']
     # url = "http://viacep.com.br/ws/"+cep+"/json"
      #print('chamou pesquisa cep')
      #print(cep)
      #print(url)
      #response = urlopen(url)
      #data = json.loads(response.read())
      #if data['uf'] == 'PE':
       # print('CEP CORRETO')
       # return JsonResponse(data)
      #else:
       # print('CEP INCORRETO')
       # return JsonResponse(data)

