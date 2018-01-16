# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='images/%Y/%m/%d/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='labels/%Y/%m/%d/'),
        ),
    ]
