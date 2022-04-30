from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse
from django.views import generic

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