from django.urls import path
from . import views
urlpatterns = [
    path('', views.registerPage),
    path('registerResult', views.registerResult)
]