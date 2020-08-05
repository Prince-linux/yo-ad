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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_of_item', models.TextField()),
                ('publisher', models.TextField()),
                ('date_published', models.DateTimeField()),
                ('description_of_item', models.TextField()),
                ('price', models.CharField(max_length=50)),
                ('category_of_item', models.CharField(max_length=50)),
                ('brand_name_of_item', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=30)),
                ('available', models.BooleanField()),
                ('approved', models.BooleanField()),
                ('promoted', models.BooleanField()),
                ('item_image', models.ImageField(upload_to='yo/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='yo.AdItem')),
            ],
        ),
    ]
