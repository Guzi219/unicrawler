# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QiuMeiMei',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'', max_length=500, verbose_name=b'\xe9\xa1\xb5\xe9\x9d\xa2\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('image', models.TextField(default=b'', max_length=500, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('update_time', models.DateTimeField(default=b'', max_length=6, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('create_time', models.DateTimeField(default=b'', max_length=6, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('uniqueid', models.CharField(default=b'', max_length=32, verbose_name=b'\xe5\x94\xaf\xe4\xb8\x80\xe6\xa0\x87\xe8\xaf\x86', blank=True)),
                ('link', models.CharField(default=b'', max_length=255, verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85\xe9\x93\xbe\xe6\x8e\xa5', blank=True)),
                ('text', models.TextField(default=b'', max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
            ],
        ),
    ]
