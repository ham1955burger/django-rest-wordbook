# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0002_word_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='image',
        ),
    ]
