from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Ad
from destinationApp.models import City
from communityApp.models import Quiz, Strategy, Visa
from noteApp.models import Note
from hotelApp.models import Hotel

# Create your views here.
def home(request):

    imgList = Ad.objects.all()

    cityList = City.objects.all()[:9]

    quizList = Quiz.objects.all().order_by("-quizDate")[:10]

    noteList = Note.objects.all().order_by("-views")[:3]

    hotelList = Hotel.objects.all().order_by("-score")[:3]

    strategyList = Strategy.objects.all().order_by("-publishDate")[:3]

    visa = Visa.objects.all().order_by("-views")[:2]

    return render(request, 'home.html', {
        'active_menu': 'home',
        'imgList': imgList,
        'cityList': cityList,
        'quizList': quizList,
        'noteList': noteList,
        'hotelList': hotelList,
        'strategyList': strategyList,
        'visa': visa,
    })
