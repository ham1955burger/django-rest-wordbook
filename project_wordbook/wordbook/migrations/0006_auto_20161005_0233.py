# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0005_auto_20161004_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]