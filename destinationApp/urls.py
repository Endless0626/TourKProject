from django.urls import path
from . import views

app_name = 'destinationApp'

urlpatterns = [
    path('city/', views.city, name='city'),
    path('special/<str:specialName>/', views.special, name='special'),
    path('citymap/', views.citymap, name='citymap'),
    path('cityDetail/<int:id>/', views.cityDetail, name='cityDetail'),
    path('citySpecial/<int:id>/<str:specialName>/', views.citySpecial, name='citySpecial'),
    path('specialDetail/<int:id>/', views.specialDetail, name='specialDetail'),
]