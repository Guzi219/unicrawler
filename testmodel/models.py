# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class article(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(default='',blank=True,verbose_name='文本')
