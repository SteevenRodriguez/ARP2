# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('foto', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/')),
                ('apellido', models.TextField(max_length=50)),
                ('direccion', models.TextField(max_length=50)),
                ('numero_telefonico', models.TextField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'Repuesto',
                'verbose_name_plural': 'Repuestos',
            },
        ),
    ]
