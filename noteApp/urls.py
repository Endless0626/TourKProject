from django.urls import path
from . import views

app_name = 'noteApp'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('route', views.routes, name='routes'),
    path('noteDetail/<int:id>/', views.noteDetail, name='noteDetail'),

]