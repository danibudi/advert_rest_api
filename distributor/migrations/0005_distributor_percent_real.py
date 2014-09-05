# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0004_remove_advertisement_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='percent_real',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=True,
        ),
    ]
