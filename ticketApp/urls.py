from django.urls import path
from . import views

app_name = 'ticketApp'

urlpatterns = [
    path('ticket/', views.ticket, name='ticket'),
    path('ticketDetail/', views.ticketDetail, name='ticketDetail'),
    # path('ticketType/<str:ticketType>/', views.ticketType, name='ticketType'),
    path('ticketOff/<str:ticketType>/<str:off>/<str:land>', views.ticketOff, name='ticketOff'),
    path('ticketSelf/', views.ticketSelf, name="ticketSelf"),
    path('search/', views.search, name='search'),
]