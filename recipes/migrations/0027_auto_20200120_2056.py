# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-20 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0026_auto_20200120_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingredient_1',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_10',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_2',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_3',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_4',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_5',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_6',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_7',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_8',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredient_9',
            field=models.CharField(blank=True, default='', max_length=54),
        ),
    ]