from django.contrib import admin
import xadmin
from .models import Quiz, Reply, Visa, visaData, visaAbout, Strategy

class ReplyInline(object):
    model = Reply
    extra = 1

class QuizAdmin(object):
    inlines = [ReplyInline, ]

class DataInline(object):
    model = visaData
    extra = 1

class AboutInline(object):
    model = visaAbout
    extra = 1

class VisaAdmin(object):
    inlines = [DataInline, AboutInline, ]

class StrategyAdmin(object):
    list_display = ['title', 'file', 'publishDate']

xadmin.site.register(Quiz, QuizAdmin)
xadmin.site.register(Visa, VisaAdmin)
xadmin.site.register(Strategy, StrategyAdmin)