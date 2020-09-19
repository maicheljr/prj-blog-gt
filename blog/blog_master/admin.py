from django.contrib import admin
from .models import Post, Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nome', 'criado', 'publicado']
    list_filter = ['nome', 'criado', 'publicado']
    search_fields = ['publicado']
    date_hierarchy = 'publicado'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'status', 'publicado']
    list_filter = ['status','criado', 'autor', 'publicado']
    readonly_fields = ['visualizar_imagem']
    search_fields = ['titulo','conteudo']
    date_hierarchy = 'publicado'
    raw_id_fields = ['autor']
    prepopulated_fields = {'slug':['titulo']}

    def visualizar_imagem(self,obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem cadastrada"
