from django.http import JsonResponse
from django.shortcuts import render
from django import forms
from captcha.fields import CaptchaField, CaptchaStore
from captcha.views import captcha_image_url
from django.contrib import messages
from Model.models import User, Teacher, Transaction
import json


class Capt(forms.Form):
    captcha = CaptchaField(
        label='验证码',
        required=True,
        error_messages={
            'required': '验证码不能为空'
        }
    )


def loginPage(request):
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    login_form = Capt()
    return render(request, 'login.html', locals())

def loginResult(requests):
    if requests.is_ajax():
        result = dict()
        result['key'] = CaptchaStore.generate_key()
        result['image_url'] = captcha_image_url(result['key'])
        print(1)
        return JsonResponse(result)
    if requests.method == 'POST':
        account = requests.POST.get('id')
        password = requests.POST.get('password')
        identity = requests.POST.get('identity')
        print('identity ', identity)
        capt = Capt(requests.POST)
        if not capt.is_valid():
            return render(requests, 'return.html', {'message': "验证码错误", 'href': "/login"})
        if account and password:
            if identity == 'Student':
                if User.objects.filter(id=account, password=password):
                    requests.session['user'] = account
                    requests.session['type'] = 'Student'
                    sellConfirm = Transaction.objects.filter(seller=requests.session['user'], status=2)
                    requests.session['message'] = len(sellConfirm)
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