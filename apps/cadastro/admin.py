from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Document, EspecieAnimal

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

class AdminMural(admin.ModelAdmin):
    list_display = ('id','nome_cachorro','especie','sexo','tipo','porte')
    list_filter = ('nome_cachorro','especie','tipo')
    list_display_links = ('id','nome_cachorro')
    ordering = ['nome_cachorro','especie']
    search_fields = ['nome_cachorro']

#admin.site.register(Document,AdminMural)
#admin.site.register(EspecieAnimal)


