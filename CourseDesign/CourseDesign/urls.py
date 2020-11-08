"""CourseDesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from .views import startPage

urlpatterns = [
    path('login/', include('Login.urls')),
    path('search/', include('SearchApp.urls')),
    path('Register/', include('Register.urls')),
    path('', startPage),
    path('admin/', admin.site.urls),
    path('goodsshowtest/', include('GoodShowTest.urls')),
    path('studentinfo/', include('StudentInfo.urls')),
    path('insertGoods/', include('Insertgoods.urls')),
    path('modifyGoods/', include('ModifyGoods.urls')),
    path('modifyInfo/', include('ModifyInfo.urls')),
    path('showInfo/', include('ShowInfo.urls')),
    path('itemInfo/', include('itemInfo.urls')),
    path('OrderCheck/', include('OrderCheck.urls')),
    path('ModifyComment/', include('ModifyComment.urls')),
    path('messages/', include('messages.urls'))
]
