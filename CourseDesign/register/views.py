from django.shortcuts import render, HttpResponse
from Login.models import Account, User
import datetime
# Create your views here.

def registerPage(requests):
    return render(requests, 'Register.html')

def registerResult(requests):
    password = requests.POST.get('password')
    confirm = requests.POST.get('passwordConfirm')
    if password != confirm:
        return HttpResponse('二次密码输入错误')
    isManager = False
    ID = requests.POST.get('account')
    name = requests.POST.get('userName')
    birthday = datetime.date(int(requests.POST.get('year')),
                             int(requests.POST.get('month')),
                             int(requests.POST.get('day')))
    isMale = True if requests.POST.get('Sex') == 'Male' else False
    college = requests.POST.get('college')
    address = requests.POST.get('Address')
    account = Account.objects.create(ID=ID, password=password, isManager=isManager)
    account.save()
    user = User.objects.create(account=account, name=name,
                               birthday=birthday, isMale=isMale,
                               college=college, address=address)
    return HttpResponse('注册成功')
