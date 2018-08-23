# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='qiubaike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'', max_length=500, verbose_name=b'url', blank=True)),
                ('image', models.TextField(default=b'', max_length=500, verbose_name=b'image', blank=True)),
                ('update_time', models.DateTimeField(default=b'', max_length=6, verbose_name=b'upt', blank=True)),
                ('create_time', models.DateTimeField(default=b'', max_length=6, verbose_name=b'crt', blank=True)),
                ('uniqueid', models.CharField(default=b'', max_length=32, verbose_name=b'uniqueid', blank=True)),
                ('link', models.CharField(default=b'', max_length=255, verbose_name=b'link', blank=True)),
                ('text', models.TextField(default=b'', max_length=100, verbose_name=b'text', blank=True)),
            ],
        ),
    ]
