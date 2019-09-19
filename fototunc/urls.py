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
from django.contrib import admin
from django.urls import path, include, re_path
# home_view import ettik view.py adresinde olan
from home.views import home_view
from contact.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # sol taraf adres sağ taraf girilecek view
    path('', home_view),
    path('tracking/', include('tracking.urls')),
    path('contact/', contact_view)
]
