# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayPromotions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('promotional_price', models.CharField(max_length=10)),
                ('promotions', models.ForeignKey(to='yo.AdItem')),
            ],
        ),
    ]
