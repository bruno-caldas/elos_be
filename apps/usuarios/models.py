from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    sigla = models.CharField(verbose_name='Sigla',max_length=2,unique=True,blank=False,null=False,help_text='Insira a sigla do estado.')
    estado = models.CharField(verbose_name='Estado',max_length=30,unique=True,blank=False,null=False,help_text='Insira o nome do estado.')
    atende = models.BooleanField(verbose_name='Atende Doação?',blank=False,null=False,help_text='O estado esta atendendo doações?')
    def __str__(self):
        return self.sigla

class DadoPessoal(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,blank=False,null=False)
    telefone_fixo = models.CharField(verbose_name='Telefone Fixo',help_text='Insira um número para contato. Exemplo: (00) 0000-0000.',max_length=14,unique=True)
    telefone_celular = models.CharField(verbose_name='Telefone Celular',help_text='Insira um número de celular para contato. Exemplo: (00) 00000-0000.',max_length=15,blank=False,null=False,unique=True)
    endereco = models.CharField(verbose_name='Endereço',help_text='Insira um endereço para retirada das doações.',max_length=250,blank=False,null=False)
    numero = models.CharField(verbose_name='Número',help_text='Insira o número do endereço',max_length=6,blank=False,null=False)
    complemento = models.CharField(verbose_name='Complemento',help_text='Insira um complemento ao endereço.',max_length=150)
    cidade = models.CharField(verbose_name='Cidade que reside',help_text='Insira sua cidade',max_length=150,blank=False,null=False)
    uf = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cep = models.CharField(verbose_name='CEP',help_text='Insira seu CEP.',max_length=9)
    def __str__(self):
        return self.usuario
