from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Quiz, Visa, Strategy
from django.shortcuts import get_object_or_404
from .forms import QuizForm, ReplyForm
from django.core.paginator import Paginator
from pyquery import PyQuery as pq
from django.http import StreamingHttpResponse, JsonResponse

import os

def strategy(request):
    strategyList = Strategy.objects.all().order_by('-publishDate')

    for doc in strategyList:
        html = pq(doc.title)
        doc.mytxt = pq(html)('p').text()

    p = Paginator(strategyList, 6)
    if p.num_pages <= 1:
        pageDate = ''
    else:
        page = int(request.GET.get('page', 1))
        strategyList = p.page(page)
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

    return render(
        request, 'strategyList.html', {
            'active_menu': 'community',
            'sub_menu': 'strategys',
            'strategyList': strategyList,
            'pageDate': pageDate,
        }
    )

def read_file(file_name, size):
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break

def getDoc(request, id):
    doc = get_object_or_404(Strategy, id=id)
    update_to, filename = str(doc.file).split('/')
    filepath = '%s/media/%s/%s' % (os.getcwd(), update_to, filename)
    response = StreamingHttpResponse(read_file(filepath, 512))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response

def quiz(request):
    if request.method == 'POST':
        quizForm = QuizForm(data=request.POST) #创建模型表单对象
        if quizForm.is_valid():
            quizForm.save() #存到数据库
            return render(request, 'successq.html')
    else:  #没有提交
            quizForm = QuizForm()  #创建模型表单对象，并传给message.html

    submenu = 'quizs'
    quizList = Quiz.objects.all()

    p = Paginator(quizList, 5)
    if p.num_pages <= 1:
        pageDate = ''
    else:
        page = int(request.GET.get('page', 1))
        quizList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page+2]
            print(total_pages)
            if right[-1] < total_pages-1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]
            right = page_range[page:page+2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages-1:
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

    return render(request, 'quiz.html', {
        'active_menu': 'community',
        'sub_menu': submenu,
        'quizList': quizList,
        'quizForm': quizForm,
        'pageDate': pageDate,
    })

def reply(request, id):

    if request.method == 'POST':
        replyForm = ReplyForm(data=request.POST) #创建模型表单对象
        if replyForm.is_valid():
            replyForm.save() #存到数据库
            return render(request, 'successr.html')
    else:  #没有提交
            replyForm = ReplyForm()  #创建模型表单对象，并传给message.html

    replyList = get_object_or_404(Quiz, id=id)

    return render(request, 'reply.html', {
        'active_menu': 'community',
        'replyList': replyList,
        'replyForm': replyForm,
    })

def visa(request):
    visaList = Visa.objects.all().order_by('-views')

    return render(request, 'visaList.html', {
        'active_menu': 'community',
        'visaList': visaList,
        'sub_menu': 'visas',
    })

def visaData(request, id):
    visadetail = get_object_or_404(Visa, id=id)
    PeopleList = visadetail.datas.all()
    peopleList = PeopleList.values('people').distinct().order_by('people')
    List = {}
    for pe in peopleList:
        peo = pe['people']
        pdList = PeopleList.filter(people=peo)
        List[peo] = pdList

    return render(
        request, 'visaDetail.html', {
            'active_menu': 'community',
            'sub_menu': 'visas',
            'visadetail': visadetail,
            'List': List,
            'peopleList': peopleList,
        }
    )

def search(request):

    if request.method == 'POST':
        quizForm = QuizForm(data=request.POST) #创建模型表单对象
        if quizForm.is_valid():
            quizForm.save() #存到数据库
            return render(request, 'successq.html')
    else:  #没有提交
            quizForm = QuizForm()  #创建模型表单对象，并传给message.html

    keyword = request.GET.get('keyword')
    quizList = Quiz.objects.filter(title__icontains=keyword)
    quizName = "关于" + "\"" + keyword + "\"" + "的搜索结果"

    return render(request, 'searchquiz.html', {
        'active_menu': 'community',
        'sub_menu': 'quizs',
        'quizName': quizName,
        'quizList': quizList,
        'quizForm': quizForm,
    })
