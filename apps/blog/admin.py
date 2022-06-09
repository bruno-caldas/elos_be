from django.contrib import admin
from blog.models import Post

# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ('id','titulo','data_publicacao')
    list_filter = ('titulo','data_publicacao')
    list_display_links = ('id','titulo','data_publicacao')
    ordering = ['data_publicacao','titulo']
    search_fields = ['titulo']

admin.site.register(Post,AdminPost)