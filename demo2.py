# -*- coding: utf-8 -*-
import re

from bs4 import BeautifulSoup

__author__ = 'guyp'

imgdata = '<noscript>&lt;img src="http://wx2.sinaimg.cn/mw690/9bd522c1gy1fdffq88n0tg209q05h4qy.gif" alt="这是最新科技,可以变成你最想要的东西" /&gt;</noscript>'
imgdata = imgdata.replace('&lt;', '<').replace('&gt;', '>')
# print imgdata
# soup = BeautifulSoup(imgdata, 'lxml')
# data = soup.find('img')
# print data['src']
#
# print BeautifulSoup(imgdata.replace('&lt;','<').replace('&gt;','>'), 'lxml').find('img')['src']

# exec("out_val = BeautifulSoup(imgdata.replace('&lt;','<').replace('&gt;','>'), 'lxml').find('img')['alt']",{})

g = {'BeautifulSoup': BeautifulSoup}
l = {"imgdata": imgdata, 'out_val': ''}
ele = re.find('123abc','[a-z]+')
print ele

exec ("out_val = BeautifulSoup(imgdata.replace('&lt;','<').replace('&gt;','>'), 'lxml').find('img')['alt']", g, l)
print out_val
