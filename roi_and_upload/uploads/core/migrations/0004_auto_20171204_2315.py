# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171204_2149'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document_images',
        ),
        migrations.AddField(
            model_name='document',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='<django.db.models.fields.CharField>/%Y/%m/%d/'),
        ),
    ]
