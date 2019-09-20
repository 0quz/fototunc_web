"""fototunc URL Configuration

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
from django.urls import path, re_path
# bütün traciking viewları içe aktardık
from .views import *
# çakışmayı engellemek için
app_name = 'tracking'

urlpatterns = [
    # sol taraf adres sağ taraf girilecek view
    path('index/', tracking_index, name='index'),
    path('create/', tracking_create, name='create'),
    # r'^ başlangıç belirtiyor /$ sonu belirtiyor
    # iç (?P<id>\d+) kısmı detail id yi sayfa ismi olarak belirliyoruz
    # re_path(r'^(?P<id>\d+)/detail/$', tracking_detail, name='detail'),
    # slug için güncelledik (w) her hangi bir karakter demek model ve view deki bütün id leri slug a çevirdik
    re_path(r'^(?P<slug>[\w-]+)/$', tracking_detail, name='detail'),
    # update için örnek tracking/4/update
    re_path(r'^(?P<slug>[\w-]+)/update/$', tracking_update, name='update'),
    # id alıp yönlendirme yapmak için
    re_path(r'^(?P<slug>[\w-]+)/delete/$', tracking_delete, name='delete'),
    re_path(r'^(?P<slug>[\w-]+)/ready/$', tracking_ready, name='ready'),
]
