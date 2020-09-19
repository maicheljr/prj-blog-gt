from django.contrib import admin
from .models import Link

# Register your models here.


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ['criado','alterado']
    list_display = ['chave', 'criado', 'alterado']
    list_filter = ['chave', 'criado', 'alterado']


