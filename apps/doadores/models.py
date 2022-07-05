from audioop import reverse
from faulthandler import disable
from pickle import TRUE
from statistics import mode

from django import forms
from django.conf import Settings, settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.urls import reverse
from requests import request
from localflavor.br.models import BRStateField, BRPostalCodeField
from django.contrib.messages.views import SuccessMessageMixin

# Create your models here.

class Doadores(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Primeiro Nome')
    sobrenome = models.CharField(max_length=50, verbose_name='Sobrenome')
    dt_nasc = models.DateField(max_length=11, verbose_name='Data de Nascimento')
    cep = BRPostalCodeField('CEP')
    endereco = models.CharField(max_length=500, verbose_name='Endereço')
    numero = models.IntegerField(verbose_name='Numero')
    complemento = models.CharField(max_length=50,verbose_name='Complemento')
    bairro = models.CharField(max_length=500, verbose_name='Bairro')
    cidade = models.CharField(max_length=500, verbose_name='Cidade')
    estado = BRStateField(null=True, blank=True, verbose_name='Estado')    
    
   
    celular = models.CharField(max_length=16, verbose_name='Celular para Contato',unique=True)
       
    DO = 'DOADOR'
    DT = 'DONATÁRIO'
                           
    intencao = (
        (DO, 'DOADOR'),
        (DT, 'DONATÁRIO'),
                
    )

    Intencao =  models.CharField(choices=intencao, verbose_name="Intenção", max_length=50)
    username = models.ForeignKey(User, on_delete=models.PROTECT, null= False, verbose_name='Doador')

    def get_absolute_url(self):
        return reverse_lazy('home')

    def __str__(self):
        return "{} {} {} ({})".format(self.nome, self.username, self.celular, self.Intencao)


   


class Doacao(models.Model):
    
    AL = 'ALIMENTOS NÃO PERECÍVEIS'
    AN = 'ANIMAIS'
    BR = 'BRINQUEDOS'
    EQ = 'EQUIPAMENTOS (CADEIRA DE RODAS, MULETA, ÓCULOS E ETC...)'
    HP = 'ITENS DE HIGIENE PESSOAL'
    LV = 'LIVROS'
    MV = 'MOVÉIS'
    RP = 'ROUPAS COMUM'
    RPC = 'ROUPAS DE FRIO E ACESSÓRIOS'
                               
    classificacao = (
        (AL, 'ALIMENTOS NÃO PERECÍVEIS'),
        (AN, 'ANIMAIS'),
        (BR, 'BRINQUEDOS'),
        (EQ, 'EQUIPAMENTOS (CADEIRA DE RODAS, MULETA, ÓCULOS E ETC...)'),
        (HP, 'ITENS DE HIGIENE PESSOAL'),
        (LV, 'LIVROS'),
        (MV, 'MOVÉIS'),
        (RP, 'ROUPAS COMUM'),
        (RPC, 'ROUPAS DE FRIO E ACESSÓRIOS'),
           
    )
    classificacao =  models.CharField(choices=classificacao, verbose_name="Tipo de Doação", max_length=56)
    
    descricao = models.CharField(max_length=3000, verbose_name='Descrição do item para doação')
    
    NV = 'NOVO'
    SM = 'SEMI-NOVO'
    US = 'USADO'
    NA = 'NAO SE APLICA AO ITEM'
                           
    listestado = (
        (NV, 'NOVO'),
        (SM, 'SEMI-NOVO'),
        (US, 'USADO'),
        (NA, 'NÃO SE APLICA'),
                
    )
    estado =  models.CharField(choices=listestado, verbose_name="Estado de Conservação", max_length=50)
    quantidade = models.IntegerField(verbose_name='Quantidade de Itens', null=False)
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=False, verbose_name='Doador' )

    def get_absolute_url(self):
        return reverse('novadoacao')

    def __str__(self):
        return "{} {} {} {} ({})".format(self.classificacao, self.descricao, self.estado, self.quantidade, self.username)
