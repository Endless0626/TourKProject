from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Hotel
from destinationApp.models import Special, City

def hotels(request):
    List = Hotel.objects.all()
    cityList = List.values('city').distinct().order_by('-city')

    htList = {}
    spList = {}
    foList = {}
    for cit in cityList:
        pla = cit['city']
        plaList = List.filter(city=pla)
        htList[pla] = plaList
        spotsList = Special.objects.all().order_by('-score').filter(specialType='景点').filter(place=pla)[:3]
        spList[pla] = spotsList

    return render(request, 'hotelList.html', {
        'active_menu': 'hotel',
        'cityList': cityList,
        'spList': spList,
        'htList': htList,
    })

def hotelDetail(request, id, photoType):
    hoteldetail = get_object_or_404(Hotel, id=id)
    hoteldetail.views += 1
    hoteldetail.save()

    List = hoteldetail.hotelImgs.all()
    TypeList = List.values('photoType').distinct().order_by('-photoType')

    priceList = hoteldetail.roomPrice.all()

    if photoType == '全部':
        imgList = hoteldetail.hotelImgs.all()
    else:
        imgList = hoteldetail.hotelImgs.all().filter(photoType=photoType)

    city = get_object_or_404(City, name=hoteldetail.city)
    n1 = get_object_or_404(Special, title=hoteldetail.near1)
    n2 = get_object_or_404(Special, title=hoteldetail.near2)
    n3 = get_object_or_404(Special, title=hoteldetail.near3)

    return render(request, 'hotelDetail.html', {
        'active_menu': 'hotel',
        'hoteldetail': hoteldetail,
        'imgList': imgList,
        'priceList': priceList,
        'TypeList': TypeList,
        'city': city,
        'n1': n1,
        'n2': n2,
        'n3': n3,
    })