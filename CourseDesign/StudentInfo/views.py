from django.shortcuts import render
from Login.models import Account, Commodity, User
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def InfoPage(request):
    tmp = User.objects.filter(account=request.session['user'])[0]
    datas = {'Account': request.session['user'], 'Name': tmp.name, 'Birthday': tmp.birthday, 'Sex': 'Male' if tmp.isMale else 'Female', 'College': tmp.college, 'Address': tmp.address}
    good_list = Commodity.objects.filter(owner=request.session['user'])
    goods = []
    for good in good_list:
        goods.append({'ID': good.ID, 'Name': good.name, 'Price': good.price, 'Description': good.description})
    return render(request, 'StudentInfo.html', {'datas': datas, 'goods': goods, 'len': len(goods)})


def DeleteItem(request):
    delete_list = request.POST.getlist('choose')
    for Id in delete_list:
        Commodity.objects.filter(ID=Id).delete()
    messages.success(request, "删除中")
    return HttpResponseRedirect('/studentinfo')
