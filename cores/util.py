# -*- coding: utf-8 -*-
from django.shortcuts import redirect

__author__ = 'yijingping'
import redis
import json
from django.conf import settings
from hashlib import md5
REDIS_POOL = None


def get_redis_pool():
    global REDIS_POOL
    if not REDIS_POOL:
        REDIS_POOL = redis.ConnectionPool(**settings.REDIS_OPTIONS)

    return REDIS_POOL


def get_redis():
    return redis.Redis(connection_pool=get_redis_pool())


def get_uniqueid(url):
    link = get_link_from_url(url)
    return md5(link).hexdigest()


def get_link_from_url(url):
    if isinstance(url, basestring):
        return url
    elif isinstance(url, dict):
        return json.dumps(url)

def checkUrlValidate(url, site_config):
    """
    检查是否以 “http(s)” 开头,
    是否 “//” 开头
    :param self:
    :param url:
    :return:
    """
    if not url.startswith('http') and not url.startswith("//"):
        url = site_config['domain'] + url
    return url

def login_required(f):
    """
    要求登录的decorator
    :param f: 函数
    :return:
    """
    def _wrapper(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated():
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        else:
            #request_context = RequestContext(request)
            #request_context.push({"admin_user": user})
            return f(request, *args, **kwargs)
    return _wrapper