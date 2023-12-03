"""
URL configuration for newDBdjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from mysite import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new_map',views.new_map, name='new_map'),
    path('current_location/', views.current_location, name='current_location'),
    path('new_current_map', views.new_current_map, name='new_current_map'),
    #overlay url
    path('parking_detail/<str:parking_code>/', views.parking_detail, name='parking_detail'),
    path('new_entire_map', views.new_entire_map, name='new_entire_map')
]
