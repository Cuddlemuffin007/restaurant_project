# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_userprofile_allergies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='allergies',
        ),
    ]