# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20170820_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=b'arp/pic_folder/'),
        ),
    ]
