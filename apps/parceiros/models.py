from django.db import models
from django.db.models import base
from djrichtextfield.models import RichTextField

# Create your models here.
class Parceiros(models.Model):
    nome_parceiro = models.CharField(max_length=100,null=False,blank=False,unique=True,verbose_name='Parceiro',help_text='Escreve o nome do Parceiro.')
    descricao_parceiro = RichTextField(default='')
    site_parceiro = models.URLField(null=True,max_length=200,verbose_name='Site',help_text='Insira o site do parceiro.')
    class Meta:
    #     db_table = 'parceiro'
        ordering = ['nome_parceiro']
    def __str__(self):
        return self.nome_parceiro
