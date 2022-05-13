from django.db import reset_queries
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse
from django.views import generic

from eventos.models import Evento
from parceiros.models import Parceiros

#CARREGA AS PÁGINAS PRINCIPAIS

def carrega_eventos(request):
    eventos = Evento.objects.all()
    return render(request,'eventos/eventos.html',{'eventos':eventos })

# Create your views here.
