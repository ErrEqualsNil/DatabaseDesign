from django.urls import path, re_path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.modifyInfo),
    path('modifyResult/', views.modifyResult),
]