# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150504_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='Food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='WiFi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
        ),
    ]
