# Generated by Django 2.2.6 on 2022-04-05 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_auto_20220404_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='receita',
            name='date_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 4, 21, 43, 12, 693570)),
        ),
    ]
