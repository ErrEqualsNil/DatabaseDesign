from django.shortcuts import render
from django.http import HttpResponseRedirect
from Model.models import Commodity,Transaction
from django.contrib import messages
# Create your views here.

def loadHTML(requests):
    sellConfirm = Transaction.objects.filter(seller=requests.session['user'], status=2)
    confirmMessages = []
    for m in sellConfirm:
        confirmMessages.append({'TID': m.id, 'buyer': m.buyer, 'commodityID': m.commodity.id,
                                'commodityName': m.commodity.name, 'commodityPrice': m.commodity.price,
                                'commodityImage': 'https://database-design.oss-cn-beijing.aliyuncs.com/' + m.commodity.image})
    return render(requests, 'messages.html', {'sellMessageLen': len(sellConfirm), 'sellMessage': confirmMessages})


def ConfirmMessage(requests):
    TID = requests.GET.get('TID')
    trans = Transaction.objects.filter(id=TID)[0]
    trans.status = 3
    trans.save()
    return render(requests, 'return.html',
                  {'message': "确认出售，请联系买家", 'href': "/messages"})

