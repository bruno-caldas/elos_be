from django.contrib import admin
from usuarios.models import DadoPessoal, Estado

class AdminDados(admin.ModelAdmin):
    list_display = ('id','telefone_celular')
    list_filter = ('usuario',)
    list_display_links = ('id','telefone_celular')

admin.site.register(DadoPessoal,AdminDados)

class AdminEstado(admin.ModelAdmin):
    list_display = ('id','sigla','estado','atende')
    list_filter = ('sigla','atende')
    list_display_links = ('id','sigla','estado')
    ordering = ['estado']
    search_fields = ['estado']

admin.site.register(Estado,AdminEstado)
