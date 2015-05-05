# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150504_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='Alcohol',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'NO'), (1, b'YES')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Bathrooms',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'NO'), (1, b'YES')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Coffee',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Outdoor_Seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'NO'), (1, b'YES')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Outlets',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (0, b'Minimal'), (0, b'Some'), (0, b'Ample')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='Seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (0, b'Minimal'), (0, b'Some'), (0, b'Ample')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='WiFi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (0, b'Spotty'), (0, b'Strong')]),
        ),
    ]
