from django.shortcuts import render, HttpResponseRedirect
from Model.models import Commodity, User, Transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
import oss2

def GoodInfo(request):
    good_list = Commodity.objects.filter(owner=request.session['user'], status=True)
    goods = []
    for good in good_list:
        goods.append({'ID': good.id, 'Name': good.name, 'Price': good.price, 'Description': good.description,
                      'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(good.image)})
    sellConfirm = Transaction.objects.filter(seller=request.session['user'], status=2)
    request.session['message'] = len(sellConfirm)



def DeleteItem(request):
    delete_list = request.POST.getlist('choose')
    key = 'LTA' + 'I4GF' + 'kNx'
    key = key + 'HzH' + 'ejr7' + 'Xj8' + 'da9o'
    password = 'QXR' + 'i6uKVthP' + 'xInBRVScB413' + 'JW5rHxi'
    auth = oss2.Auth(key, password)
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, 'database-design')
    for Id in delete_list:
        bucket.delete_object(str(Commodity.objects.filter(id=Id)[0].image))
        Commodity.objects.filter(id=Id).delete()
    return HttpResponseRedirect('/studentinfo')
