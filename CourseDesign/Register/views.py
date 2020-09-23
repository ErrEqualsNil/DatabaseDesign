from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from Model.models import User
import datetime
# Create your views here.

def registerPage(requests):
    return render(requests, 'Register.html')


def registerResult(requests):
    password = requests.POST.get('password')
    confirm = requests.POST.get('passwordConfirm')
    if password != confirm:
        return HttpResponse('二次密码输入错误')
    id = requests.POST.get('id')
    name = requests.POST.get('userName')
    birthday = datetime.date(int(requests.POST.get('year')),
                             int(requests.POST.get('month')),
                             int(requests.POST.get('day')))
    isMale = True if requests.POST.get('Sex') == 'Male' else False
    college = requests.POST.get('college')
    address = requests.POST.get('address')
    qq = requests.POST.get('qq')
    tel = requests.POST.get('tel')
    email = requests.POST.get('email')

    try:
        user = User.objects.create(id=id, name=name, password=password,
                                   birthday=birthday, isMale=isMale,
                                   college=college, address=address,
                                   QQ=qq, tel=tel,
                                   email=email)
    except Exception as e:
        messages.success(requests, "Account already exist")
        return HttpResponseRedirect('/Register')
    return render(requests, 'return.html', {'message': "注册成功", 'href': "/login"})
