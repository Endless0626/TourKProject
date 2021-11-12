from django.contrib import admin
from .models import Ticket, selfService
from django.utils.safestring import mark_safe
import xadmin

class TicketAdmin(object):
    list_display = ['ticketType', 'airportType', 'number', 'off', 'offTime', 'land', 'siteType']

class TicketSelfAdmin(object):
    list_display = ['Name', 'Code', 'Home', 'logo_data']
    def logo_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px" />' % obj.Logo.url)

xadmin.site.register(Ticket, TicketAdmin)
xadmin.site.register(selfService, TicketSelfAdmin)