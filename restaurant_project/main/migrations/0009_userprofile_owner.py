# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_order_allergies'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Restaurant'),
        ),
    ]
