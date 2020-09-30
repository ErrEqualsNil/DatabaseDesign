from django.urls import path
from . import views
urlpatterns = [
    path('', views.loadHTML),
    path(r'messageConfirm/', views.ConfirmMessage),
]