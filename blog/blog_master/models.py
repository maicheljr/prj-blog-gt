from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super(PublicadosManager, self).get_queryset()\
                                            .filter(status='publicado')


class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),

    )

    titulo  = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250)#https://site.com/noticias/pagina-sobre-2020/01/02/2020
    autor   = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')# por default sempre vai para rascunho, alguém precisa publicar

    # por default vai pegar todos os registros
    object_list = models.Manager()


    # se criar um Manager para pesquisa , necessariamente precisa setar o 'objects' antes, na sequência adicionar o Manager customizado
    publicados = PublicadosManager() # como usar o MANAGER na view -> Post.publicados.all()]

    def get_absolute_url(self):
        return reverse('detalhe-post', args=[self.pk])

    class Meta:
        ordering = ['-publicado']

    def __str__(self):
        # return '{} - {}'.format(self.titulo, self.conteudo) # concatenando string no return
        return self.titulo



