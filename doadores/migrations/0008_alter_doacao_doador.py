# Generated by Django 3.2.5 on 2022-06-14 12:28

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0007_alter_doadores_doador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='Doador',
            field=models.CharField(max_length=50, verbose_name=django.contrib.auth.models.User),
        ),
    ]
