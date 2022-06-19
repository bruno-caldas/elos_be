from django.db import models

class Pesquisa(models.Model):

    cep = models.IntegerField(verbose_name='Pesquisa de CEP')

    