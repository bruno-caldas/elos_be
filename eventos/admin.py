from django.contrib import admin
from eventos.models import Evento

# Register your models here.

class AdminEvento(admin.ModelAdmin):
    list_display = ('id','nome_evento','data_evento')
    list_filter = ('nome_evento','data_evento')
    list_display_links = ('id','nome_evento','data_evento')
    ordering = ['data_evento','data_evento']
    search_fields = ['nome_evento']

admin.site.register(Evento,AdminEvento)