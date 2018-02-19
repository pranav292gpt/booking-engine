# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-19 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0013_auto_20171229_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='offer_applied',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Offer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='reward_applied',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Reward'),
        ),
    ]