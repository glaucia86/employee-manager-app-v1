# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 02:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeelist',
            old_name='departament',
            new_name='department',
        ),
    ]
