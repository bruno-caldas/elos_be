# Generated by Django 3.2.5 on 2022-06-14 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0002_doacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doacao',
            old_name='Intenção',
            new_name='Estado',
        ),
    ]
