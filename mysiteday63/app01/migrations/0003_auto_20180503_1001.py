# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-03 02:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher_id',
            new_name='publisher',
        ),
    ]
