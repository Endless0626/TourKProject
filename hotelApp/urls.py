from django.urls import path
from . import views

app_name = 'hotelApp'

urlpatterns = [
    path('hotels/', views.hotels, name='hotels'),
    path('hotelDetail/<int:id>/<str:photoType>', views.hotelDetail, name='hotelDetail')
]