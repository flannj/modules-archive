# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170521_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]