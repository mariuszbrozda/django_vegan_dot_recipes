# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-01 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20191230_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipe_category_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='to_be_listed',
        ),
    ]