from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import City
from .models import Special
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Count
from hotelApp.models import Hotel

def city(request):

    cityList = City.objects.all().order_by('-views')

    p = Paginator(cityList, 9)
    if p.num_pages <= 1:
        pageDate = ''
    else:
        page = int(request.GET.get('page', 1))
        cityList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageDate = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }

    return render(request, 'city.html', {
        'active_menu': 'destination',
        'sub_menu': 'city',
        'cityList': cityList,
        'pageDate': pageDate,
    })

def special(request, specialName):
    submenu = specialName
    if specialName == 'spots':
        specialName = '景点'
    elif specialName == 'entertain':
        specialName = '娱乐'
    else:
        specialName = '美食'

    specialList = Special.objects.all().filter(
        specialType=specialName).order_by('-score')

    p = Paginator(specialList, 4)
    if p.num_pages <= 1:
        pageDate = ''
    else:
        page = int(request.GET.get('page', 1))
        specialList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageDate = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }
    return render(request, 'special.html', {
        'active_menu': 'destination',
        'sub_menu': submenu,
        'specialName': specialName,
        'specialList': specialList,
        'pageDate': pageDate,
    })

def citymap(request):
    return render(request, 'ditu.html', {
        'active_menu': 'destination',
        'sub_menu': 'city',
    })

def cityDetail(request, id):
    product = get_object_or_404(City, id=id)
    product.views += 1
    product.save()

    return render(request, 'cityDetail.html', {
        'active_menu': 'destination',
        'product': product,
    })

def citySpecial(request, id, specialName):
    products = get_object_or_404(City, id=id)
    products.views += 1
    products.save()

    submenu = specialName
    if specialName == 'spots':
        specialName = '景点'
    elif specialName == 'entertain':
        specialName = '娱乐'
    else:
        specialName = '美食'

    specialAll = Special.objects.all().filter(place=products.name).filter(specialType=specialName)

    p = Paginator(specialAll, 4)
    if p.num_pages <= 1:
        pageDate = ''
    else:
        page = int(request.GET.get('page', 1))
        specialAll = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageDate = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }

    return render(request, 'citySpecial.html', {
        'active_menu': 'destination',
        'sub_menu': submenu,
        'specialName': specialName,
        'specialAll': specialAll,
        'products': products,
        'pageDate': pageDate,
    })

def specialDetail(request, id):
    special = get_object_or_404(Special, id=id)
    city = get_object_or_404(City, name=special.place)
    special.views += 1
    special.save()

    hotelList = Hotel.objects.all()
    hotels = []
    for ho in hotelList:
        if ho.near1 == special.title:
            hotels.append(ho.title)
        elif ho.near2 == special.title:
            hotels.append(ho.title)
        elif ho.near3 == special.title:
            hotels.append(ho.title)
    hotel = []
    for ho in hotels:
        hotel.append(get_object_or_404(Hotel, title=ho))

    hotel = hotel[:3]

    return render(request, 'specialDetail.html', {
        'active_menu': 'destination',
        'special': special,
        'city': city,
        'hotel': hotel,
    })

def imgCount(request, id):
    special = get_object_or_404(Special, id=id)
    result = Count(special.specialImgs.all())

    return render(request, 'specialDetail.html', {
        'active_menu': 'destination',
        'result': result,
    })