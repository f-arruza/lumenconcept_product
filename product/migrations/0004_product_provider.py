# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-10 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.CharField(default=123, max_length=36, verbose_name='Provider'),
            preserve_default=False,
        ),
    ]
