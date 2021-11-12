from django.contrib import admin
import xadmin
from .models import Ad

xadmin.site.register(Ad)