# Generated by Django 4.0.4 on 2022-04-25 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0005_rename_membro_membro_bando'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bando',
            name='quantidade_membros',
        ),
    ]
