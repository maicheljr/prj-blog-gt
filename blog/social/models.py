from django.db import models
# Create your models here.

class Link(models.Model):
    chave = models.SlugField(verbose_name="Identificação da Rede", max_length=200,unique=True)
    descricao =models.CharField(verbose_name="Descrição", max_length=200)
    url = models.URLField(max_length=200,null=False,blank=False)
    criado = models.DateTimeField(auto_now=True)
    alterado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ['chave']

    def __str__(self):
        return self.chave