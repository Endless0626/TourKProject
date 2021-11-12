from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Ticket
from .models import selfService
from pyquery import PyQuery as pq
import xlwt
from io import BytesIO
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from hotelApp.models import Hotel

def ticket(request):
    tickets = Ticket.objects.all().order_by('offTime', 'off', 'price')[:12]

    return render(
        request, 'ticketList.html', {
            'active_menu': 'ticket',
            'tickets': tickets,
        }
    )

def ticketDetail(request):

    ticketsList = Ticket.objects.all().order_by('offTime', 'off')

    return render(
        request, 'ticketDetail.html', {
            'active_menu': 'ticket',
            'ticketsList': ticketsList,
        }
    )

def ticketOff(request, ticketType, off, land):
    if ticketType == '全部':
        ticketsList = Ticket.objects.all().order_by('offTime', 'off')
        offList = ''
        landList = ''
        type_menu = 'type全部'
        ht = '韩国'
        hotelList = Hotel.objects.all().order_by('-score')[:4]

    elif ticketType == '韩国-中国':
        ticketsList = Ticket.objects.all().filter(ticketType=ticketType).order_by('offTime', 'off')
        List = Ticket.objects.filter(ticketType=ticketType)
        offList = List.values('off').distinct().order_by('off')
        landList = List.values('land').distinct().order_by('land')
        type_menu = ticketType
        ht = off
        hotelList = Hotel.objects.all().filter(city=off).order_by('-score')[:4]

    else:
        ticketsList = Ticket.objects.all().filter(ticketType=ticketType).order_by('offTime', 'off')
        List = Ticket.objects.filter(ticketType=ticketType)
        offList = List.values('off').distinct().order_by('off')
        landList = List.values('land').distinct().order_by('land')
        type_menu = ticketType
        ht = land
        hotelList = Hotel.objects.all().filter(city=land).order_by('-score')[:4]

    if off == "全部":
        ticketsList = ticketsList
        off_menu = 'off全部'
    else:
        ticketsList = ticketsList.all().filter(off=off).order_by('offTime')
        off_menu = off

    if land == "全部":
        ticketsList = ticketsList
        land_menu = 'land全部'
    else:
        ticketsList = ticketsList.all().filter(land=land).order_by('offTime')
        land_menu = land

    return render(
        request, 'ticketDetail.html', {
            'active_menu': 'ticket',
            'ticketsList': ticketsList,
            'ticketType': ticketType,
            'offList': offList,
            'landList': landList,
            'off': off,
            'land': land,
            'ht': ht,
            'type_menu': type_menu,
            'off_menu': off_menu,
            'land_menu': land_menu,
            'hotelList': hotelList,
        }
    )

def ticketSelf(request):

    selfList = selfService.objects.all().order_by('Name')

    return render(request, 'selfService.html', {
        'active_menu': 'ticket',
        'selfList': selfList,
    })

# def ticketImgs(request):
#
#     ImgsList = Ticket.objects.all().order_by('offTime', 'off')
#
#     return render(
#         request, 'ticketDetail.html', {
#             'active_menu': 'ticket',
#             'ImgsList': ImgsList,
#         }
#     )

def search(request):
    offkey = request.GET.get('offkey')
    landkey = request.GET.get('landkey')
    # offTimekey = request.GET.get('offTimekey')
    ticketsList = Ticket.objects.filter(off__icontains=offkey)\
        .filter(land__icontains=landkey)\
        # .filter(offTime__icontains=offTimekey)
    ticketName = "关于" + "\"" + offkey + "到" + landkey + "\"" + "的搜索结果"
    return render(request, 'searchTickets.html', {
        'active_menu': 'ticket',
        'ticketName': ticketName,
        'ticketsList': ticketsList,
    })
