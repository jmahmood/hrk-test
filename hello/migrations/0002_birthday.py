# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-01 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateField(verbose_name=b'Birthday')),
                ('bd', models.DateField(verbose_name=b'Birthday')),
            ],
        ),
    ]
