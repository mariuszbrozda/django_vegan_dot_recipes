# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-18 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_auto_20200118_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uploaded_by',
            field=models.CharField(default='', max_length=54),
        ),
    ]
