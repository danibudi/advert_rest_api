# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0005_distributor_percent_real'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributor',
            name='percent_real',
        ),
        migrations.AddField(
            model_name='distributor',
            name='shown_adverts',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='banner',
            field=models.ImageField(help_text=b'Please, upload gif, png format', upload_to=b'banner_immages/', null=True, verbose_name=b'Banner Image', blank=True),
        ),
    ]
