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
from localflavor.br.models import BRStateField, BRPostalCodeField, BRCPFField
from django.contrib.messages.views import SuccessMessageMixin

# Create your models here.

class Doadores(models.Model):
    #nome = models.CharField(max_length=50, verbose_name='Primeiro Nome')
    #sobrenome = models.CharField(max_length=50, verbose_name='Sobrenome')
    username = models.OneToOneField(User, on_delete=models.PROTECT, null= False, verbose_name='Doador',unique=True)
    dt_nasc = models.DateField(max_length=11,verbose_name='Data de Nascimento',help_text='Insira data de nascimento')
    celular = models.CharField(max_length=16, verbose_name='Celular para Contato',help_text='Insira o número de telefone',unique=True)
    cpf = BRCPFField(verbose_name='CPF',help_text='Cadastro de Pessoa Física',max_length=11)
    cep = BRPostalCodeField(max_length=9, verbose_name='CEP',help_text='Insira o CEP')
    endereco = models.CharField(max_length=500, verbose_name='Endereço',help_text='Insira o endereço')
    numero = models.IntegerField(verbose_name='Numero',help_text='Insira o número do endereço')
    complemento = models.CharField(max_length=50,verbose_name='Complemento',help_text='Insira o complemento do endereço')
    bairro = models.CharField(max_length=500, verbose_name='Bairro',help_text='Insira o bairro')
    cidade = models.CharField(max_length=500, verbose_name='Cidade',help_text='Insira a cidade')
    estado = BRStateField(null=True, blank=True, verbose_name='Estado',help_text='Insira o estado')
    local_referencia = models.CharField(max_length=50,verbose_name='Local de referência',help_text='Local de referência para facilitar a localização')

    class Meta:
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'
        ordering = ['username',]

    def __str__(self):
        return "{}".format(self.username.get_full_name())
    def get_absolute_url(self):
        return reverse_lazy('home')

class Doacao(models.Model):

    DO = 'DOAR' #'DOADOR'
    DT = 'RECEBER'     #'DONATÁRIO'
                          
    intencao = (
        (DO, 'DOAR'),
        (DT, 'RECEBER')         
    )

    intencao =  models.CharField(choices=intencao, verbose_name="Intenção do Donativo", max_length=50)
    
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
        (RPC, 'ROUPAS DE FRIO E ACESSÓRIOS')
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
        (NA, 'NÃO SE APLICA')
    )
    estado =  models.CharField(choices=listestado, verbose_name="Estado de Conservação", max_length=50)
    quantidade = models.IntegerField(verbose_name='Quantidade de Itens', null=False)
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=False, verbose_name='Doador' )
    def get_absolute_url(self):
        return reverse('novadoacao')
    def __str__(self):
        return "{} {} {} {} ({})".format(self.classificacao, self.descricao, self.estado, self.quantidade, self.username)
