from django.shortcuts import render, HttpResponseRedirect
from Model.models import Commodity, User, Transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
import oss2

def GoodInfo(request):
    good_list = Commodity.objects.filter(status=True)
    goods = []
    for good in good_list:
        goods.append({'ID': good.id, 'Name': good.name, 'Price': good.price, 'Description': good.description, 'Owner':good.owner,
                      'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(good.image)})
    return render(request, 'teachers.html', {
        'goods': goods,

    })
def TransInfo(request):
    trans_list1 = Transaction.object.filter()
    transl = []
    for trans in trans_list:
        transl.append({'ID': trans.id, 'Buyer': trans.buyer, 'Seller': trans.seller, 'Comment': trans.comment})
    return render(request, 'teacher.html', {
        'transl': transl,
    })




