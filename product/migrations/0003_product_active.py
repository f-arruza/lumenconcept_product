# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180308_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]