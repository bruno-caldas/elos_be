from django.contrib import admin
from .models import Doadores, Doacao, Classificacao, Receptor

class DoadoresAdmin(admin.ModelAdmin):
    list_display = ['username','dt_nasc','cpf']
    list_filter = ['estado','cidade']
    ordering = ['username',]
    search_fields = ['cpf',]
    list_per_page = 25

class DoacaoAmmin(admin.ModelAdmin):
    list_display = ['descricao','status','intencao','classificacao','publicar']
    list_filter = ['classificacao',]
    list_editable = ['publicar',]
    ordering = ['descricao',]
    search_fields = ['descricao',]
    list_por_page = 25

class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ['sintetica','analitica']
    list_filter = ['sintetica',]
    search_fields = ['analitica',]
    list_por_page = 25

class ReceptorAdmin(admin.ModelAdmin):
    list_display = ['receptor','donativo','status_contrato']
    ordering = ['data_vigencia',]
    list_filter = ['status_contrato',]
    list_por_page = 25

admin.site.register(Doadores,DoadoresAdmin)
admin.site.register(Doacao,DoacaoAmmin)
admin.site.register(Classificacao,ClassificacaoAdmin)
admin.site.register(Receptor,ReceptorAdmin)
