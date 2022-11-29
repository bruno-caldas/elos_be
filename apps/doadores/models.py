import re
from requests import request
from audioop import reverse
from faulthandler import disable
from pickle import TRUE
from statistics import mode

from django import forms
from django.conf import Settings, settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

from localflavor.br.models import BRStateField, BRPostalCodeField, BRCPFField

# Create your models here.

class Doadores(models.Model):
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

class Classificacao(models.Model):
    sintetica = models.CharField(verbose_name='Classificação Sintética',help_text='Digite a classificação sintética',max_length=30,null=False,blank=False)
    analitica = models.CharField(verbose_name='Classificação Analítica',help_text='Digite a classificação analítica',max_length=50,null=False,blank=False)
    class Meta:
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'
        ordering = ['sintetica','analitica']
        unique_together = [['sintetica','analitica']]
    def __str__(self):
        return f"{self.sintetica}: {self.analitica}"

re_matricula = re.compile('[a-zA-z]{4}-[0-9]{6}')

class Doacao(models.Model):

    DO = 'DOAR' #'DOADOR'
    DT = 'RECEBER'     #'DONATÁRIO'
                          
    intencao = (
        (DO, 'DOAR'),
        (DT, 'RECEBER')         
    )
    
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
    
    publicar = models.BooleanField(verbose_name='Publicar?',help_text='O donativo deve ser publicado na página de doações?',default=False)
    matricula = models.CharField(verbose_name='Número de matricula',help_text='Insira o número de matricula conforme exemplo: AAAA-999999',max_length=11,
        blank=True)
    status = models.CharField(verbose_name='Status',help_text='Qual situação o donativo se encontra?',
        null=False,blank=False,max_length=4,default='CDOA',
        choices=[
            ('DOADOR',(
                ('CDOA','COM DOADOR'),
                ('ADOA','AGUARDANDO ENTREGA DO DOADOR'),)),
            ('RECEPTOR',(
                ('CREC','COM RECEPTOR'),
                ('AREC','AGUARDANDO RETIRADA DO RECEPTOR'),)),
            ('MANUTENÇÃO',(
                ('MREP','NECESSITANDO REPARO'),
                ('MPEC','AGUARDANDO PEÇA'),
                ('MHIG','EM HIGIENIZAÇÃO'),)),
            ('PROJETO',(
                ('PDOC','DISPONÍVEL PARA DOAÇÃO'),
                ('POBS','OBSOLETO'),)),
            ('UNKN','UNKNOWN'),
        ])
    descricao = models.CharField(max_length=3000, verbose_name='Donativo',help_text='Escreva o nome do item')
    intencao =  models.CharField(choices=intencao, verbose_name="Intenção do Donativo",help_text='Qual a intenção do donativo?',max_length=50)
    tamanho = models.CharField(verbose_name='Tamanho',help_text='Qual o tamanho do item?',
        null=False,blank=False,max_length=1,default='P',
        choices=[
            ('P','PEQUENO'),
            ('M','MÉDIO'),
            ('G','GRANDE'),
        ])
    detalhamento = models.TextField(verbose_name='Detalhamento',help_text='Escreva um detalhamento do donativo',
        max_length=250,null=False,blank=False)
    classificacao = models.ForeignKey(Classificacao,verbose_name='Classificação',help_text='Escolha a classificação do item',
        on_delete=models.PROTECT,null=False,blank=False)
    estado =  models.CharField(choices=listestado, verbose_name="Estado de Conservação", help_text='Qual o estado de conservação do item?',max_length=50)
    quantidade = models.IntegerField(verbose_name='Quantidade de Itens', null=False)
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=False, verbose_name='Doador' )

    class Meta:
        verbose_name = 'Donativo'
        verbose_name_plural = 'Donativos'
        ordering = ['descricao',]

    def __str__(self):
        return "({}) {} {}".format(self.matricula,self.descricao,self.username.get_full_name())
    def get_absolute_url(self):
        return reverse('novadoacao')

class Receptor(models.Model):
    donativo = models.ForeignKey(Doacao,verbose_name='Donativo',help_text='Escolho o donativo',
        on_delete=models.PROTECT,null=False,blank=False)
    mensagem = models.CharField(verbose_name='Mensagem Elos de Amos',help_text='Status da Mensagem',
        null=False,blank=False,max_length=4,default='RECP',
        choices=[
            ('RECP','RECEPTOR ENVIOU'),
            ('DOAR','DOADOR RECEBEU'),
        ])
    status_contrato = models.CharField(verbose_name='Status',help_text='Doador assinou e devolveu o contrato?',
        null=False,blank=False,max_length=3,default='RECP',
        choices=[
            ('ASS','ASSINADO'),
            ('DEV','DEVOLVIDO'),
        ])
    data_vigencia = models.DateField(verbose_name='Data',help_text='Data de vigência do contrato')
    receptor = models.ForeignKey(User,on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
    
    def __str__(self):
        return "{} {} {}".format(self.donativo.matricula,self.status_contrato,self.mensagem)

