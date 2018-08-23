# -*- coding: utf-8 -*-
from io import StringIO
from xml.etree import ElementTree

from lxml import etree

class XPathExtractor():
    def __init__(self, content, rule):
        htmlparser = etree.HTMLParser(remove_comments=True)
        self.tree = etree.parse(StringIO(content), htmlparser)
        self.rule = rule

    def extract(self):
        return self.tree.xpath(self.rule)

content = u"""<!DOCTYPE html>
<html lang="zh-CN" xml:lang="zh-CN">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">
	<meta name="renderer" content="webkit">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">

	<meta name="keywords" content="JFinal, JFinal Weixin, JFinal demo, JFinal 微信, JFinal 项目, JFinal 案列, JFinal 插件, JFinal 教程" />
	<meta name="description" content="JFinal 极速开发项目集合, JFinal 优秀项目收录, JFinal 学习资源, JFinal 教程, JFinal 案例, JFinal 实战" />
	<title>JFinal 极速开发项目</title>

	<link rel="icon" type="image/x-icon" href="/assets/img/favicon.ico">
	<link rel="stylesheet" type="text/css" href="/assets/css/jfinal-com-v1.0.css?v=2120">
    <link rel="stylesheet" type="text/css" href="/assets/css/jfinal-com-my-space-v1.0.css?v=19">
    <link rel="stylesheet" type="text/css" href="/assets/iconfont/iconfont.css">



</head>

<body>
<!-- 头部容器 -->
<div class="jf-header-box">
	<!-- logo容器 -->
	<h3 class="jf-logo-box">
		<a href="/" title="返回首页">JFinal</a>
	</h3>

	<!-- 导航菜单容器 -->
	<ul class="jf-nav-menu-box">
		<li><a href="/">首页</a></li>
		<li><a href="/doc">文档 </a></li>
		<li><a href="/project">项目</a></li>
		<li><a href="/share">分享</a></li>
		<li><a href="/feedback">反馈</a></li>
		<li><a href="/club">俱乐部</a></li>
		<li><a href="/donate">捐助</a></li>
	</ul>

		<!-- 未登录用户 -->
		<div class="jf-no-login">
			<span><a href="/login" onclick="appendReturnUrl(this)">登录</a></span>
			<span><a href="/reg">注册</a></span>
		</div>

</div>


<!-- 中部主体容器 -->
<div class="jf-body-box clearfix">
<!-- 内容容器 -->
<div class="jf-panel-box jf-pull-left">

	<!-- 项目 -->
	<div class="jf-panel">
		<h2 class="jf-panel-name">项目</h2>
		<ul class="jf-panel-list">
				<li>
					<div class="jf-panel-img">
						<a href="/user/81747"><img src="/upload/avatar/x.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/119">在SQl文件里面分页</a></h3>
						<p>
							不用JFinal自带的分页，，怎么在.sql文件里面进行分页，，是直接在Where条件后面limit的吗？
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/68765"><img src="/upload/avatar/13/68765.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/120">QuickJob敏捷可配快速的任务调度平台</a></h3>
						<p>

						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/30894"><img src="/upload/avatar/6/30894.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/121">jfinal_mall</a></h3>
						<p>

						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/72285"><img src="/upload/avatar/x.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/124">jFinal Auto 敏捷开发</a></h3>
						<p>

						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/44403"><img src="/upload/avatar/8/44403.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/125">jfinal 控制反转</a></h3>
						<p>
							应用场景：            1、动态注册路由
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/44403"><img src="/upload/avatar/8/44403.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/126">jfinal 导入 导出</a></h3>
						<p>
							https://gitee.com/duaicxx/excel-utils 源码开放 使用案例在readme中支持 javabean 导入 与jfinal model 导入有问题加群：470
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/14439"><img src="/upload/avatar/2/14439.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/141">JFinal 万能CMS系统,极速开发,动态生成数据属性</a></h3>
						<p>
							JFinal 万能CMS系统,极速开发,动态生成数据属性,自定义标签，动态/静态化，一键生成模板代码。技术框架MVC：JFinal 3.3页面:freemarker
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/19049"><img src="/upload/avatar/3/19049.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/165">开源个JFinal+Vue后台项目</a></h3>
						<p>
							项目地址：https://gitee.com/xiaoxustudent/JFinal-vue-element-admin&lt;
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/56630"><img src="/upload/avatar/11/56630.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/166">应波总号召，再简单的项目也可以分享出来layui+jfinal简易后台</a></h3>
						<p>
							首先说明，很多东西都是我搬运过来的，如有雷同或侵权，请联系删除！联系方式：490244211@qq.com采用分离开发的好像是，记不清了。体验连接：http://www.fangdengfu
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/20082"><img src="/upload/avatar/4/20082.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/167">jfinal搭建的个人酷炫博客</a></h3>
						<p>
							项目地址：www.zyl.me
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/40407"><img src="/upload/avatar/8/40407.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/168">jfinal-layui-blog： Jfinal+layui整合的轻量级博客</a></h3>
						<p>

						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/14439"><img src="/upload/avatar/2/14439.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/169">JFinal O2O商城系统,支持手机端和PC端</a></h3>
						<p>
							JFinalO2O商城系统,支持手机端和PC端,基于JFinal万能CMS系统开发。技术框架MVC：J
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/14439"><img src="/upload/avatar/2/14439.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/170">JFinal B2C商城系统,支持手机端和PC端</a></h3>
						<p>
							JFinal B2c商城系统,支持手机端和PC端,基于JFinal万能CMS系统开发。技术框架MVC：
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/36688"><img src="/upload/avatar/7/36688.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/172">jboot-admin使用jboot开发的后台管理开源项目</a></h3>
						<p>
							项目地址：https://gitee.com/rlaxuc/jboot-admin项目介绍jboot-admin是基于强大的微服务框架jboot
						</p>
					</div>
				</li>
				<li>
					<div class="jf-panel-img">
						<a href="/user/22476"><img src="/upload/avatar/4/22476.jpg"></a>
					</div>
					<div class="jf-panel-item">
						<h3><a href="/project/173">LuceneX</a></h3>
						<p>
							LuceneX 是一个简单、轻便、快速、独立、可扩展的Java 全文检索框架。尤其是自带的强大分词器和动态数据源功能特点：
						</p>
					</div>
				</li>
		</ul>

		<!-- 分页 -->
<ul class="jf-paginate">
	<li><a href="/project?p=4" class="pre-page">&lt;</a></li>
	<li><a href="/project?p=1">1</a></li>
	<li><a href="/project?p=2">2</a></li>
	<li><a href="/project?p=3">3</a></li>
	<li><a href="/project?p=4">4</a></li>
	<li><a href="javascript:void(0);" class="current-page">5</a></li>
	<li><a href="/project?p=6">6</a></li>
	<li><a href="/project?p=6" class="next-page">&gt;</a></li>
</ul>
	</div>

</div>

<!-- 包含侧边栏文件 -->
<!-- 侧边栏容器 -->
<div class="jf-sidebar-box jf-pull-right">

<div class="jf-sidebar jf-adv-panel">

	<h4 class="jf-sidebar-name">赞助商<span class="jf-red-dot" style="margin-left: 15px;"></span></h4>

	<div class="jf-adv-panel-main">
		<a href="http://www.ukewo.cn/" target="_blank" rel="nofollow"
		title="优客服 - 开源的智能客服系统 + 呼叫中心"
		   time-limit="2018-06-20 0:0:0">优客服 - 开源的智能客服系统 + 呼叫中心</a>
	</div>


	<div class="jf-adv-panel-main">
		<a href="http://www.dbumama.com" target="_blank" rel="nofollow"
		style="background-color: #009688;"
		title="点步微拼团 - 专业的微信拼团软件"
		   time-limit="2018-07-20 0:0:0">点步微拼团 - 专业的微信拼团软件</a>
	</div>

	<div class="jf-adv-panel-main">
		<a href="http://www.layui.com/admin/" target="_blank" rel="nofollow"
		style="background-color: #252630"
		title="layuiAdmin - 通用后台管理模板"
		   time-limit="2018-07-26 0:0:0">layuiAdmin - 通用后台管理模板</a>
	</div>

</div>
	<!-- 侧边栏 -->
	<div class="jf-sidebar">
		<h4 class="jf-sidebar-name">热门项目</h4>
		<ul class="jf-sidebar-hot-list">
				<li><a href="/project/1">JFinal 极速开发框架</a></li>
				<li><a href="/project/2">JFinal Weixin 极速开发 SDK</a></li>
				<li><a href="/project/3">JPress ，一个wordpress的java代替版</a></li>
				<li><a href="/project/4">【有更新】JBolt-JFinal极速开发IDE插件（Eclipse、Idea）</a></li>
				<li><a href="/project/6">JFinal Weixin 极速开发Demo</a></li>
				<li><a href="/project/7">JFinal-event（JFinal事件驱动插件）</a></li>
				<li><a href="/project/8">JFinal-assets（线上css、js压缩插件）</a></li>
				<li><a href="/project/9">JFinal快速开发平台</a></li>
				<li><a href="/project/11">更好用的Java社区 - 朋也社区</a></li>
				<li><a href="/project/13">kungfu， 基于JFinal的微服务框架</a></li>
		</ul>
	</div>



<div class="jf-sidebar" style="text-align: center;min-height:250px;">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 300_600 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:600px"
     data-ad-client="ca-pub-7445243974946854"
     data-ad-slot="3534814315"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div></div></div>

<!-- 底部容器 -->
<div class="jf-footer-box">
	<ul>
		<li><a href="/share/1" target="_blank">关于JFinal</a></li>
		<li><a href="javascript:void(0);">友情链接</a></li>
		<li><a href="http://git.oschina.net/jfinal/jfinal" target="_blank">开源中国git</a></li>
		<li><script src="http://s5.cnzz.com/z_stat.php?id=1000336597&web_id=1000336597" language="JavaScript"></script></li>

		<li><a href="http://www.miitbeian.gov.cn/" target="_blank">京ICP备10217229号-2</a></li>
	</ul>
</div>
<script type="text/javascript" src="/assets/js/jquery.min-v1.11.3.js"></script>
<script type="text/javascript" src="/assets/js/jfinal-com-v1.0.js?v=18"></script>
</body>
</html>"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'unicrawler.settings'
import django
django.setup()
# xpathEx = XPathExtractor(content,"//div[contains(@class,'article block')]/a[@class='contentHerf']/div[@class='content']/span")
xpathEx = XPathExtractor(content,"//ul[@class='jf-panel-list']/li")
result = xpathEx.extract()
print (len([result]))
print type(result)
for r in result:
    if isinstance(r, etree._Element):
        r =  ElementTree.tostring(r, encoding='utf-8', method='html')
    print r
    # print type(r)

# print str('ISO').upper().startswith("ISO")

# defaults = {"name":"value","id":"pk"}
# for k, v in defaults.iteritems():
#     print k, v
#
# unique_key = ["id","id2","thid"]
# data = {"id":"1", "id2":"2","thid":"3"}
# result = ':'.join(['%s' % data[k] for k in unique_key])
# print result


# import MySQLdb
#
# # 打开数据库连接
# db = MySQLdb.connect("192.168.0.169", "root", "123456", "unicrawler", charset='utf8mb4' )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("""SELECT
# 	t.url,
# 	t.link,
# 	t.id,
# 	t.image,
# 	t.text
# FROM
# 	data_qiubaike t
# WHERE
# 	t.link = '/article/120606483'""")
#
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
# for r in data:
#     print r
# # print "Database version : %s " % data['text']
#
# # 关闭数据库连接
# db.close()