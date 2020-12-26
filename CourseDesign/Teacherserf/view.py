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



)
