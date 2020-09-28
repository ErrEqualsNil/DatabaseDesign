from django.urls import path
from . import views

urlpatterns = [
    path('', views.itemInfo),
    path(r'finishPurchase/', views.finishPurchase),
]
