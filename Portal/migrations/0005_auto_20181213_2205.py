# Generated by Django 2.1.3 on 2018-12-13 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0004_auto_20181213_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='createdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
