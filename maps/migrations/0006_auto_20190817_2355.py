# Generated by Django 2.2.4 on 2019-08-17 22:55

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_auto_20190817_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='bike_shops',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='surfaces',
            field=models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]