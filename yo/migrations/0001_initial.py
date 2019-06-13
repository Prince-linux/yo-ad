# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_item', models.TextField()),
                ('publisher', models.TextField()),
                ('date_published', models.DateTimeField()),
                ('description_of_item', models.TextField()),
                ('price', models.CharField(max_length=1)),
                ('category_of_item', models.CharField(max_length=1, choices=[(b'ELECTRONICS', b'electronics'), (b'HOUSING & REAL ESTATES', b'housing & real estates'), (b'FURNITURE', b'furniture'), (b'FOOD', b'food'), (b'CLOTHING', b'clothing'), (b'VEHICLES & BIKES', b'vehicles & bikes'), (b'BOOKS', b'books')])),
                ('brand_name_of_item', models.CharField(max_length=1, choices=[(b'HP', b'hp'), (b'SAMSUNG', b'samsung'), (b'APPLE', b'apple'), (b'LG', b'lg'), (b'TOSHIBA', b'toshiba'), (b'LAND ROVER', b'land rover'), (b'MERCEDES', b'mercedes'), (b'OTHER', b'other')])),
                ('location', models.CharField(max_length=1, choices=[(b'ACCRA', b'accra'), (b'KUMASI', b'kumasi'), (b'TEMA', b'tema'), (b'KOFORIDUA', b'koforidua'), (b'TAKORADI', b'takoradi'), (b'WINNEBA', b'winneba'), (b'TAMALE', b'tamale'), (b'WA', b'wa'), (b'BOLGATANGA', b'bolgatanga'), (b'SUNYANI', b'sunyani'), (b'SEKONDI', b'sekondi'), (b'CAPE-COAST', b'cape-coast'), (b'HO', b'ho')])),
                ('contact', models.CharField(max_length=1)),
                ('available', models.BooleanField()),
                ('approved', models.BooleanField()),
                ('item_image', models.ImageField(upload_to=b'yo/images/')),
            ],
        ),
    ]
