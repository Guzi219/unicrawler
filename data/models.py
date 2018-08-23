# -*- coding: utf-8 -*-
__author__ = 'guyp'
from django.db import models


# Create your models here.
class qiubaike(models.Model):
    url = models.CharField(max_length=500, blank=True, default='', verbose_name='url')
    image = models.TextField(max_length=500, blank=True, default='', verbose_name='image')
    update_time = models.DateTimeField(max_length=6, blank=True, default='', verbose_name='upt')
    create_time = models.DateTimeField(max_length=6, blank=True, default='', verbose_name='crt')
    uniqueid = models.CharField(max_length=32, blank=True, default='', verbose_name='uniqueid')
    link = models.CharField(max_length=255, blank=True, default='', verbose_name='link')
    text = models.TextField(max_length=100, blank=True, default='', verbose_name='text')

    def __unicode__(self):
        return self.text[:8]

    class Meta:
        verbose_name_plural = "1 糗事百科"

class QiuMeiMei(models.Model):
    url = models.CharField(max_length=500, blank=True, default='', verbose_name='页面地址')
    image = models.TextField(max_length=500, blank=True, default='', verbose_name='图片')
    update_time = models.DateTimeField(max_length=6, blank=True, default='', verbose_name='更新时间')
    create_time = models.DateTimeField(max_length=6, blank=True, default='', verbose_name='创建时间')
    uniqueid = models.CharField(max_length=32, blank=True, default='', verbose_name='唯一标识')
    link = models.CharField(max_length=255, blank=True, default='', verbose_name='详情链接')
    text = models.TextField(max_length=100, blank=True, default='', verbose_name='标题')

    def __unicode__(self):
        return self.text[:8]

    class Meta:
        verbose_name_plural = "2 糗妹妹动图"

class jfinal(models.Model):
    url = models.CharField(max_length=500, blank=True, default='', verbose_name='页面地址')
    headpic = models.CharField(max_length=100, blank=True, default='', verbose_name='头像')
    update_time = models.DateTimeField(max_length=6, blank=True, default='', verbose_name='更新时间')
    create_time = models.DateTimeField(max_length=6, blank=True, default='', verbose_name='创建时间')
    uniqueid = models.CharField(max_length=32, blank=True, default='', verbose_name='唯一标识')
    link = models.CharField(max_length=255, blank=True, default='', verbose_name='详情链接')
    title = models.CharField(max_length=255, blank=True, default='', verbose_name='标题')
    text = models.TextField(max_length=500, blank=True, default='', verbose_name='文章简介')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "3 JFinal"
