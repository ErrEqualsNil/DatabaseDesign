from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def startPage(requests):
    return render(requests, "Search.html")

