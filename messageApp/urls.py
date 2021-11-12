from django.urls import path
from .import views


app_name = 'messageApp'

urlpatterns = [
    path('message/', views.message, name='message'),# 欢迎留言
    path('showreply/', views.showreply, name='showreply'),# 留言回复
    path('about/', views.about, name='about'),
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),
]