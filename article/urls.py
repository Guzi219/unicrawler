# -*- coding: utf-8 -*-
__author__ = 'guyp'
from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^$', view.index),
    url(r'^addname$', view.addname, name="wechat.add")
]
