# Generated by Django 2.1.3 on 2018-12-12 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 12, 23, 22, 29, 728132)),
        ),
    ]
