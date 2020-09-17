from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Account

def loginPage(request):
    return render(request, 'login.html')

def loginResult(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    if account and password:
        if Account.objects.filter(ID=account, password=password):
            return HttpResponse("Login Success!")
        else:
            return HttpResponse("Password Wrong!")
    else:
        return HttpResponse("Access Denied!")