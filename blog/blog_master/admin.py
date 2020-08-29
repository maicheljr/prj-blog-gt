from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)

class Postdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'status', 'publicado']
    list_filter = ['status','criado', 'autor', 'publicado']
    search_fields = ['titulo','conteudo']
    date_hierarchy = 'publicado'
    raw_id_fields = ['autor']
    prepopulated_fields = {'slug':['titulo']}
