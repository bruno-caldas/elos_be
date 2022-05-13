from django.db import models
from datetime import datetime, timedelta

from parceiros.models import Parceiros

data_atual = datetime.now()

# Create your models here.
class Evento(models.Model):
    nome_evento = models.CharField(blank=False,null=False,unique=True,max_length=100,verbose_name='Nome do Evento',help_text='Insira o nome do evento.')
    descricao_evento = models.TextField(blank=False,null=False,unique=True,verbose_name='Descrição do Evento',help_text='Faça uma breve descrição sobre o evento.')
    local_evento = models.CharField(max_length=150,verbose_name='Local do Evento',help_text='Exemplo: Rua, número, Bairro, CEP, Município, UF')
    data_evento = models.DateTimeField(verbose_name='Data do Evento',help_text='Data de realização do evento.')
    parceiros = models.ManyToManyField(Parceiros,verbose_name='Parceiros',help_text='Insira os parceiros do evento.')
    class Meta:
    #     db_table = 'evento' #nome definido da tabela no DB
        ordering = ['data_evento','nome_evento']
    def __str__(self): #correção para admin.py na aparecer como object
        return self.nome_evento
    def get_data_evento(self): #função para retornar a data formatada
        return self.data_evento.strftime('%d/%m/%Y %H:%M')
    def get_evento_recente(self):
        if self.data_evento >= data_atual:
            return True
        else:
            return False
    def get_evento_vencido(self):
        if self.data_evento < data_atual:
            return True
        else:
            return False
    def get_parceiros(self):
        busca_parceiros = list(self.parceiros.all())
        if busca_parceiros!=0:
            lista_parceiros = []
            arruma_lista = Parceiros()
            for arruma_lista in busca_parceiros:
                arruma_lista = arruma_lista.nome_parceiro
                lista_parceiros.append(arruma_lista)
            return lista_parceiros
        else:
            return False
    def get_falta(self):
        data = self.data_evento
        falta = data - data_atual
        if falta.days >= 365:
            return '%sY' %int(falta.days / 365)
        elif falta.days >= 30:
            return '%sM' %int(falta.days / 30)
        else:
            return '%sd' %falta.days