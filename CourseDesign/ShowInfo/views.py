from django.shortcuts import render
from django.http import HttpResponseRedirect
from Model.models import Commodity, User
# Create your views here.


def showInfo(requests):
    id = requests.GET.get('id')
    tmp = User.objects.filter(id=id)[0]
    datas = {'ID': id, 'Name': tmp.name, 'Sex': 'Male' if tmp.isMale else 'Female', 'College': tmp.college,
             'Address': tmp.address, 'QQ': tmp.QQ, 'Tel': tmp.tel, 'Email': tmp.email}
    good_list = Commodity.objects.filter(owner=id, status=True)
    return render(requests, 'ShowInfo.html', {'datas': datas, 'goods': good_list, 'len': len(good_list)})
