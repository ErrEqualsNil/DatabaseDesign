from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .models import Account
import json
def loginPage(request):
    return render(request, 'login.html')

def loginResult(requests):
    account = requests.POST.get('account')
    password = requests.POST.get('password')
    if account and password:
        if Account.objects.filter(ID=account, password=password):
            requests.session['user'] = account
            return render(requests, 'return.html', {'message': "登录成功", 'href': "/search"})
        else:
            return render(requests, 'return.html', {'message': "账号或密码错误", 'href':"/login"})
    else:
        return render(requests, 'return.html', {'message': "请输入账号密码", 'href':"/login"})

def reLogin(requests):
    requests.session.flush()
    return render(requests, 'return.html', {'message': "退出登录成功", 'href':"/login"})