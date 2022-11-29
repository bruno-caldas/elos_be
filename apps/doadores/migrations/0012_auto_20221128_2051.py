# Generated by Django 3.2.5 on 2022-11-28 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0011_auto_20221128_1940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classificacao',
            options={'ordering': ['sintetica', 'analitica'], 'verbose_name': 'Classificação', 'verbose_name_plural': 'Classificações'},
        ),
        migrations.AlterField(
            model_name='doacao',
            name='classificacao',
            field=models.ForeignKey(help_text='Escolha a classificação do item', on_delete=django.db.models.deletion.PROTECT, to='doadores.classificacao', verbose_name='Classificação'),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='descricao',
            field=models.CharField(help_text='Escreva o nome do item', max_length=3000, verbose_name='Donativo'),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='estado',
            field=models.CharField(choices=[('NOVO', 'NOVO'), ('SEMI-NOVO', 'SEMI-NOVO'), ('USADO', 'USADO'), ('NAO SE APLICA AO ITEM', 'NÃO SE APLICA')], help_text='Qual o estado de conservação do item?', max_length=50, verbose_name='Estado de Conservação'),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='intencao',
            field=models.CharField(choices=[('DOAR', 'DOAR'), ('RECEBER', 'RECEBER')], help_text='Qual a intenção do donativo?', max_length=50, verbose_name='Intenção do Donativo'),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='matricula',
            field=models.CharField(blank=True, help_text='Insira o número de matricula conforme exemplo: AAAA-999999', max_length=11, verbose_name='Número de matricula'),
        ),
    ]