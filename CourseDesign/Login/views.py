from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def login_view(request):
    return render(request, 'login.html')

def loginResult(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    if account and password:
        return HttpResponse("Login Successfully！")
    else:
        return HttpResponse("Access Denied!")