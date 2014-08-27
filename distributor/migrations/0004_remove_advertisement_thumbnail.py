# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0003_auto_20140824_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='thumbnail',
        ),
    ]
