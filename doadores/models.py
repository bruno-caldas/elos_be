from django.db import models

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

    