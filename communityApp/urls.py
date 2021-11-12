from django.urls import path
from . import views

app_name = 'communityApp'

urlpatterns = [
    path('strategy/', views.strategy, name='strategy'),
    path('quiz/', views.quiz, name='quiz'),
    path('reply/<int:id>/', views.reply, name='reply'),
    path('visa/', views.visa, name='visa'),
    path('visaData/<int:id>/', views.visaData, name='visaData'),
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),
    path('search/', views.search, name='search'),
    # path('quizdelete/<int:id>', views.quizdelete, name='quizdelete')
    # path('replydelete/<int:id>/<int:id>/', views.replydelete, name='replydelete')
]