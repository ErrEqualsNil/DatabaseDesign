from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from Login.models import Account, User, Teacher
import datetime


# Create your views here.

def registerPage(requests):
    return render(requests, 'AdminRegister.html')


def registerResult(requests):
    password = requests.POST.get('password')
    confirm = requests.POST.get('passwordConfirm')
    if password != confirm:
        return HttpResponse('二次密码输入错误')
    isManager = True
    ID = requests.POST.get('account')
    name = requests.POST.get('userName')
    isMale = True if requests.POST.get('Sex') == 'Male' else False

    try:
        account = Account.objects.create(ID=ID, password=password, isManager=isManager)
        teacher = Teacher.objects.create(account=account, name=name,
                                         isMale=isMale)
    except Exception:
        messages.success(requests, "Account already exist")
        return HttpResponseRedirect('/adminregister')

    requests.session['user'] = ID
    return render(requests, 'return.html', {'message': "注册成功", 'href': "/search"})


# Create your views here.
