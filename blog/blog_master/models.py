from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
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

    class Meta:
        ordering = ['-publicado']

    def __str__(self):
        # return '{} - {}'.format(self.titulo, self.conteudo)
        return self.titulo



