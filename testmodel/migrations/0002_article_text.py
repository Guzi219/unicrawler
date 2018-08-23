# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe6\x9c\xac', blank=True),
        ),
    ]
