# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_qiumeimei'),
    ]

    operations = [
        migrations.CreateModel(
            name='jfinal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'', max_length=500, verbose_name=b'\xe9\xa1\xb5\xe9\x9d\xa2\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('headpic', models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
                ('update_time', models.DateTimeField(default=b'', max_length=6, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('create_time', models.DateTimeField(default=b'', max_length=6, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('uniqueid', models.CharField(default=b'', max_length=32, verbose_name=b'\xe5\x94\xaf\xe4\xb8\x80\xe6\xa0\x87\xe8\xaf\x86', blank=True)),
                ('link', models.CharField(default=b'', max_length=255, verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85\xe9\x93\xbe\xe6\x8e\xa5', blank=True)),
                ('title', models.CharField(default=b'', max_length=255, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('text', models.TextField(default=b'', max_length=500, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xae\x80\xe4\xbb\x8b', blank=True)),
            ],
            options={
                'verbose_name_plural': '3 JFinal',
            },
        ),
        migrations.AlterModelOptions(
            name='qiubaike',
            options={'verbose_name_plural': '1 \u7cd7\u4e8b\u767e\u79d1'},
        ),
        migrations.AlterModelOptions(
            name='qiumeimei',
            options={'verbose_name_plural': '2 \u7cd7\u59b9\u59b9\u52a8\u56fe'},
        ),
    ]
