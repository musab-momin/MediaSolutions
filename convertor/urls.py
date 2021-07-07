from os import name
from django.contrib import admin
from django.urls import path
from convertor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('makechange', views.makechange, name='imagechanger')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
