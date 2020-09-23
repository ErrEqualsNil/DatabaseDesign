from django.urls import path
from . import views
urlpatterns = [
    path('', views.modifyGoods),
    path('', views.modifyResult)
]