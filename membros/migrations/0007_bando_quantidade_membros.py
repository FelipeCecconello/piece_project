# Generated by Django 4.0.4 on 2022-04-25 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0006_remove_bando_quantidade_membros'),
    ]

    operations = [
        migrations.AddField(
            model_name='bando',
            name='quantidade_membros',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
