# Generated by Django 3.2.5 on 2022-05-12 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20211127_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['nome_cachorro', 'data_nascimento', 'tipo', 'porte']},
        ),
        migrations.AlterModelOptions(
            name='especieanimal',
            options={'ordering': ['especie']},
        ),
    ]
