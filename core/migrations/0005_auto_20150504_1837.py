# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='Alcohol',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='Bathrooms',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='Coffee',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='Food',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='Outdor_Seating',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='Outlets',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='Seating',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='WiFi',
            field=models.TextField(null=True, blank=True),
        ),
    ]
