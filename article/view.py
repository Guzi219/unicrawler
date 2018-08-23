# -*- coding: utf-8 -*-
import json
import requests
from io import StringIO
from lxml import etree
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, redirect, HttpResponseRedirect, render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponse

from cores.util import login_required
from testmodel.models import article

CRAWLER_CONFIG = settings.CRAWLER_CONFIG

import logging
logging.basicConfig()

@login_required
def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context=context)

def addname(request):
    test1 = article(name='runoob', text = '''


在饭店正点菜呢，一个风骚的老娘们扭进来了，直接无视我的存在，对服务员说:“两份干锅鱼头打包，急”，服务员答“对不起，这位美女先来的，请您稍等一下.“她，哼~!~剜了我一眼站到我旁边。<br>呦~哇靠! :“鱼头还有几个？”<br>服务员：“四个。”<br>“我都要了！”<br>结账时才知道那老娘们是老板娘……上当了……

''')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

