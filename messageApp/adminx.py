from django.contrib import admin
from .models import Message, Protocol
import xadmin
from django.utils.safestring import mark_safe

class MessageAdmin(object):
    list_display = ('name', 'phone', 'email', 'title', 'content')

class ProtocolAdmin(object):
    list_display = ('title', 'publishDate')

xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Protocol, ProtocolAdmin)

# Register your models here.
