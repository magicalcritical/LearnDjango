# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='sub1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub3',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub4',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub5',
            field=models.IntegerField(),
        ),
    ]
