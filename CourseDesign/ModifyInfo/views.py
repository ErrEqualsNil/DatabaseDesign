from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from Model.models import User
import datetime, time
# Create your views here.


def modifyInfo(requests):
    account = requests.GET.get('account')
    tmp = User.objects.filter(id=account)[0]
    datas = {'ID': account, 'Name': tmp.name, 'Birthday': tmp.birthday, 'IsMale': tmp.isMale, 'College': tmp.college,
             'Address': tmp.address, 'QQ': tmp.QQ, 'Tel': tmp.tel, 'Email': tmp.email}
    return render(requests, 'ModifyInfo.html', {'datas': datas})


def modifyResult(requests):
    account = requests.GET.get('account')
    new_password = requests.POST.get('newPassword')
    confirm = requests.POST.get('passwordConfirm')
    if new_password != confirm:
        return HttpResponse('二次密码输入错误')
    if requests.POST.get('originalPassword') != User.objects.filter(id=account)[0].password:
        return HttpResponse('原始密码输入错误')
    name = requests.POST.get('userName')
    year = int(requests.POST.get('year'))
    month = int(requests.POST.get('month'))
    day = int(requests.POST.get('day'))
    try:
        time.strptime(str(year) + " " + str(month) + " " + str(day), "%Y %m %d")
    except Exception as e:
        return HttpResponse('日期错误')
    birthday = datetime.date(year, month, day)
    isMale = True if requests.POST.get('Sex') == 'Male' else False
    college = requests.POST.get('college')
    address = requests.POST.get('address')
    qq = requests.POST.get('qq')
    tel = requests.POST.get('tel')
    email = requests.POST.get('email')
    try:
        if new_password:
            user = User.objects.filter(id=account).update(password=new_password)

        user = User.objects.filter(id=account).update(name=name, email=email,
                                                      birthday=birthday, isMale=isMale,
                                                      college=college, address=address,
                                                      QQ=qq, tel=tel)
        return HttpResponseRedirect('/studentinfo')
    except Exception as e:
        return render(requests, 'return.html',
                      {'message': "修改失败，请检查输入", 'href': "/studentinfo"})
