# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0006_auto_20140903_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='banner',
            field=models.ImageField(help_text=b'Please, upload gif, png format', upload_to=b'banner_immages/', verbose_name=b'Banner Image'),
        ),
    ]
