# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yo', '0002_paypromotions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayPromotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('promotional_price', models.CharField(max_length=10)),
                ('promotion', models.OneToOneField(to='yo.AdItem')),
            ],
        ),
        migrations.RemoveField(
            model_name='paypromotions',
            name='promotions',
        ),
        migrations.DeleteModel(
            name='PayPromotions',
        ),
    ]
