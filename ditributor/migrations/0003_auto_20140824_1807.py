# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ditributor', '0002_auto_20140824_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='banner',
            field=models.ImageField(help_text=b'Please, upload gif, png format', upload_to=b'banner_immages/', verbose_name=b'Banner Image'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='thumbnail',
            field=models.ImageField(upload_to=b'doc100/', editable=False),
        ),
    ]
