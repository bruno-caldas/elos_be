from django.contrib import admin
from .models import Doadores, Doacao

class DoadoresAdmin(admin.ModelAdmin):
    list_display = ['username','dt_nasc','cpf']
    list_filter = ['estado','cidade']
    ordering = ['username',]
    search_fields = ['cpf',]
    list_per_page = 25

admin.site.register(Doadores,DoadoresAdmin)
admin.site.register(Doacao)
