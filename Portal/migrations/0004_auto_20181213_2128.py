# Generated by Django 2.1.3 on 2018-12-13 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0003_auto_20181212_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 13, 21, 28, 59, 104080)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='tips',
            field=models.ForeignKey(default=None, on_delete=None, to='Portal.Tips'),
        ),
    ]