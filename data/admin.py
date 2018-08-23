from django.contrib import admin
from data.models import qiubaike
from data.models import QiuMeiMei
from data.models import jfinal
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'text', 'create_time')
    list_filter = ['url']
    search_fields = ['text']

admin.site.register(qiubaike, ArticleAdmin)

class QiuMMAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'text', 'create_time')
    list_filter = ['url']
    search_fields = ['text']

admin.site.register(QiuMeiMei, QiuMMAdmin)

class jfinalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'create_time')
    list_filter = ['url']
    search_fields = ['title']

admin.site.register(jfinal, jfinalAdmin)