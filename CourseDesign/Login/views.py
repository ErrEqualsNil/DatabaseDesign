from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from Model.models import User, Teacher
import json
def loginPage(request):
    return render(request, 'login.html')

def loginResult(requests):
    account = requests.POST.get('id')
    password = requests.POST.get('password')
    identity = requests.POST.get('identity')
    print('identity ', identity)
    if account and password:
        if identity == 'Student':
            if User.objects.filter(id=account, password=password):
                requests.session['user'] = account
                requests.session['type'] = 'Student'
                return render(requests, 'return.html', {'message': "登录成功", 'href': "/search"})
            else:
                return render(requests, 'return.html', {'message': "账号或密码错误", 'href':"/login"})
        else:
            if Teacher.objects.filter(id=account, password=password):
                requests.session['user'] = account
                requests.session['type'] = 'Teacher'
                return render(requests, 'return.html', {'message': "登录成功", 'href': "/search"})
            else:
                return render(requests, 'return.html', {'message': "账号或密码错误", 'href':"/login"})
    else:
        return render(requests, 'return.html', {'message': "请输入账号密码", 'href':"/login"})

def reLogin(requests):
    requests.session.flush()
    return render(requests, 'return.html', {'message': "退出登录成功", 'href':"/login"})