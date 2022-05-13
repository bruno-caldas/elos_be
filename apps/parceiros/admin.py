from typing import ClassVar
from django.contrib import admin

from parceiros.models import Parceiros

# Register your models here.
class AdminParceiro(admin.ModelAdmin):
    list_display = ('id','nome_parceiro')
    list_filter = ['nome_parceiro']
    list_display_links = ('id','nome_parceiro')
    ordering = ['nome_parceiro']
    search_fields = ['nome_parceiro']

admin.site.register(Parceiros,AdminParceiro)
