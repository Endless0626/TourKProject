from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Note
from pyquery import PyQuery as pq
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from destinationApp.models import Special, City

def routes(request):
    noteList = Note.objects.all().order_by("-views")

    for mynew in noteList:
        html = pq(mynew.description)
        mynew.mytxt = pq(html)('p').text()

    spotsList = Special.objects.all().order_by('-score').filter(specialType='景点')[:2]
    entertainList = Special.objects.all().order_by('-score').filter(specialType='娱乐')[:2]
    foodList = Special.objects.all().order_by('-score').filter(specialType='美食')[:2]

    p = Paginator(noteList, 8)
    if p.num_pages <= 1:
        pageDate = ''
    else:
        page = int(request.GET.get('page', 1))
        noteList = p.page(page)
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

    return render(request, 'noteList.html', {
        'active_menu': 'news',
        'noteList': noteList,
        'pageDate': pageDate,
        'spotsList': spotsList,
        'entertainList': entertainList,
        'foodList': foodList,
    })

def noteDetail(request, id):
    noteList = Note.objects.all().filter(~Q(id=id)).order_by("-views")[:6]

    notes = get_object_or_404(Note, id=id)
    notes.views += 1
    notes.save()

    return render(request, 'noteDetail.html', {
        'active_menu': 'note',
        'noteList': noteList,
        'notes': notes,
    })

def upload(request):
    return render(request, 'noteUpload.html', {
        'active_menu': 'note',
    })