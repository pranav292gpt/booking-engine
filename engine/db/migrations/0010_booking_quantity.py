# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-23 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_site_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='quantity',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]