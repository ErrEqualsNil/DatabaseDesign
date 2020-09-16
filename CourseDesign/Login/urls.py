from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('loginResult', views.loginResult)
]
