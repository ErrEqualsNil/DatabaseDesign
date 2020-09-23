from django.urls import path
from . import views
urlpatterns = [
    path('', views.insertGoodsPage),
    path('insertResult', views.insertGoodsResult),
]