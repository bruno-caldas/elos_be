# Generated by Django 3.2.5 on 2022-07-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0002_alter_doadores_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doadores',
            name='celular',
            field=models.CharField(max_length=16, unique=True, verbose_name='Celular para Contato'),
        ),
    ]
