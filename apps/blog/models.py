from django.db import models
from datetime import datetime, timedelta

data_atual = datetime.now()

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(blank=False,null=False,unique=True,max_length=100,verbose_name='Título da publicação',help_text='Insira o título para sua publicação.')
    publicacao = models.TextField(blank=False,null=False,unique=True,verbose_name='Publicação',help_text='Digite sua publicação.')
    data_publicacao = models.DateTimeField(verbose_name='Publicação em',help_text='Data de publicação.',auto_now=True)
    class Meta:
        db_table = 'blog' #nome definido da tabela no DB
        ordering = ['data_publicacao','titulo']
    def __str__(self): #correção para admin.py na aparecer como object
        return self.titulo
    def get_data_publicacao(self): #função para retornar a data formatada
        return self.data_publicacao.strftime('%d/%m/%Y %H:%M')
    def get_publicacao_recente(self):
        if self.data_publicacao >= data_atual:
            return True
        else:
            return False
    def get_publicacao_antiga(self):
        if self.data_publicacao < data_atual:
            return True
        else:
            return False
    def get_publicacao(self):
        data = self.data_publicacao
        falta = data - data_atual
        if falta.days >= 365:
            return '%sY' %int(falta.days / 365)
        elif falta.days >= 30:
            return '%sM' %int(falta.days / 30)
        else:
            return '%sd' %falta.days