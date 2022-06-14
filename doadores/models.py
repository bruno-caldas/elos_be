 
from faulthandler import disable
from statistics import mode

from django import forms
from django.conf import Settings, settings
from django.db import models
from django.contrib.auth.models import User
from requests import request

# Create your models here.

class Doadores(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Primeiro Nome')
    sobrenome = models.CharField(max_length=50, verbose_name='Sobrenome')
    dt_nasc = models.DateField(max_length=11, verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=500, verbose_name='Endereço')
    numero = models.IntegerField(verbose_name='Numero')
    complemento = models.CharField(max_length=50,verbose_name='Complemento')
    celular = models.IntegerField(verbose_name='Celular para Contato',unique=True)
       
    DO = 'DOARDOR'
    DT = 'DONATÁRIO'
                           
    intencao = (
        (DO, 'DOADOR'),
        (DT, 'DONATÁRIO'),
                
    )

    Intenção =  models.CharField(choices=intencao, verbose_name="Intenção", max_length=50)
    Doador = models.OneToOneField(User, on_delete=models.CASCADE)

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
    Classificacao =  models.CharField(choices=classificacao, verbose_name="Estado de Conservação", max_length=56)
    
    Descricao = models.CharField(max_length=50, verbose_name='Descrição do item para doação')
    
    NV = 'NOVO'
    SM = 'SEMI-NOVO'
    US = 'USADO'
    NA = 'NAO SE APLICA AO ITEM'
                           
    estado = (
        (NV, 'NOVO'),
        (SM, 'SEMI-NOVO'),
        (US, 'USADO'),
        (NA, 'NÃO SE APLICA'),
                
    )
    Estado =  models.CharField(choices=estado, verbose_name="Estado de Conservação", max_length=50)
    Quantidade = models.IntegerField(verbose_name='Quantidade de Itens')
    Doador = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    
    
   

      
    