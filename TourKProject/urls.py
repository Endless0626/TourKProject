"""TourKProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from homeApp.views import home
from django.conf import settings
from django.conf.urls.static import static
import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('destinationApp/', include('destinationApp.urls')),
    path('ticketApp/', include('ticketApp.urls')),
    path('hotelApp/', include('hotelApp.urls')),
    path('search/', include('haystack.urls')),
    path('noteApp/', include('noteApp.urls')),
    path('communtityApp/', include('communityApp.urls')),
    path('messageApp/', include('messageApp.urls')),
    path('', home, name='home'),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('xadmin/', xadmin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
