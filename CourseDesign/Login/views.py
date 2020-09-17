from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import UserAccount, ManagerAccount

def loginPage(request):
    return render(request, 'login.html')

def loginResult(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    if account and password:
        if UserAccount.objects.filter(userAccount=account, userPassword=password):
            return HttpResponse("Login Success!")
        else:
            return HttpResponse("Wrong Account!")
    else:
        return HttpResponse("Access Denied!")