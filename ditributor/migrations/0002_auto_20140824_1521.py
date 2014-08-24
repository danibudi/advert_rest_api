# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ditributor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='thumbnail',
            field=models.ImageField(default=datetime.date(2014, 8, 24), upload_to=b'^admin/doc100/', editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='banner',
            field=models.ImageField(help_text=b'Please, upload jpg, gif, png format', upload_to=b'banner_immages/', verbose_name=b'Banner Image'),
        ),
    ]
