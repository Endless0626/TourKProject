from django.contrib import admin
from .models import City
from .models import Special, SpecialImg
import xadmin

class CityAdmin(object):
    list_display = ['name', 'enname', 'description', 'photo']

class SpecialImgInline(object):
    list_display = ['title', 'kname', 'score', 'publishDate']
    model = SpecialImg
    extra = 1

class SpecialAdmin(object):
    inlines = [SpecialImgInline, ]

xadmin.site.register(City, CityAdmin)
xadmin.site.register(Special, SpecialAdmin)

xadmin.site.site_header = '企业门户网站后台管理系统'
xadmin.site.site_title = '企业门户网站后台管理系统'
