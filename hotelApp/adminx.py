from django.contrib import admin
from django.forms import CheckboxSelectMultiple

from .models import MainFacility, Service, HotelFacility, RoomFacility,\
    Hotel, RoomPrice, HotelImgs, UserComment
import xadmin
from django import forms

class HotelImgInline(object):
    model = HotelImgs
    extra = 1

class RoomPriceInline(object):
    model = RoomPrice
    extra = 1

class UserCommentInline(object):
    model = UserComment
    extra = 1

class HotelFrom(forms.ModelForm):
    mfacility = forms.ModelMultipleChoiceField(widget=CheckboxSelectMultiple, queryset=MainFacility.objects.all())
    service = forms.ModelMultipleChoiceField(widget=CheckboxSelectMultiple, queryset=Service.objects.all())
    hfacility = forms.ModelMultipleChoiceField(widget=CheckboxSelectMultiple, queryset=HotelFacility.objects.all())
    rfacility = forms.ModelMultipleChoiceField(widget=CheckboxSelectMultiple, queryset=RoomFacility.objects.all())


class HotelAdmin(object):
    form = HotelFrom
    inlines = [HotelImgInline, RoomPriceInline, UserCommentInline, ]

xadmin.site.register(MainFacility)
xadmin.site.register(Service)
xadmin.site.register(HotelFacility)
xadmin.site.register(RoomFacility)
xadmin.site.register(Hotel, HotelAdmin)
