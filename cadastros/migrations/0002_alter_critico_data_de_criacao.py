# Generated by Django 4.1 on 2022-10-25 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critico',
            name='data_de_criacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 10, 25, 15, 34, 16, 237993)),
        ),
    ]
