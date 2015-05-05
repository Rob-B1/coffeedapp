# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150504_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='Outdor_Seating',
            new_name='Outdoor_Seating',
        ),
    ]
