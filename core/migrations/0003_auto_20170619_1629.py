# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_publication_state_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha'),
        ),
    ]