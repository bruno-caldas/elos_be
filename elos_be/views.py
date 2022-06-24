from cgitb import reset
from tokenize import group
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.views.generic import TemplateView


#CARREGA AS PÁGINAS PRINCIPAIS

def carrega_index(request):
    return render(request, "templates/../index.html")

def carrega_abrigo(request):
    return render(request, "templates/../abrigo.html")

def carrega_contatos(request):
    return render(request, "templates/../contatos.html")

def carrega_ajuda(request):
    return render(request, "templates/../ajuda.html")

def carrega_resgate(request):
    return render(request, "templates/../resgate.html")

#def carrega_aplicacao(request):
 #   return render(request, "templates/../home.html")

class PaginaHome(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'templates/../home.html' 
