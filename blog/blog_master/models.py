from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe


class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super(PublicadosManager, self).get_queryset()\
                                            .filter(status='publicado')

class Category(models.Model):
    nome = models.CharField(max_length=100)
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now=True)
    alterado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
        verbose_name= "Categoria"
        verbose_name_plural= "Categorias"

    def __str__(self):
        return self.nome

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),

    )

    titulo  = models.CharField(verbose_name="Título",max_length=250)
    slug    = models.SlugField(max_length=250)#https://site.com/noticias/pagina-sobre-2020/01/02/2020
    autor   = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Category, related_name="get_posts")
    imagem = models.ImageField(upload_to="blog", blank=True, null=True)
    conteudo = RichTextField(verbose_name='Conteúdo')
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

    def get_absolute_url_detail(self):
        return reverse('detalhe-post', args=[self.pk])

    def get_absolute_url_update(self):
        return reverse('update-post', args=[self.pk])

    def get_absolute_url_delete(self):
        return reverse('delete-post', args=[self.pk])

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px"/>'%self.imagem.url)
        view_image.short_description = "Imagem cadastrada"
        view_image.allow_tags = True

    class Meta:
        ordering = ['-publicado']

    def __str__(self):
        # return '{} - {}'.format(self.titulo, self.conteudo) # concatenando string no return
        return self.titulo




# usando um signal pra testar se o slug foi preenchido, se está vazio ele completa automaticamente com o slugify
@receiver(post_save,sender=Post)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()


