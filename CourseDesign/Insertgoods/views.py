from django.shortcuts import render
from django.http import HttpResponseRedirect
from Model.models import Commodity
from django.contrib import messages
# Create your views here.


def insertGoodsPage(requests):
    return render(requests, 'insertGoods.html')


def insertGoodsResult(requests):
    itemName = requests.POST.get('itemName')
    itemPrice = requests.POST.get('itemPrice')
    itemDescription = requests.POST.get('itemDescription')
    try:
        item = Commodity.objects.create(name=itemName, price=itemPrice,
                                        description=itemDescription, owner=requests.session['user'],
                                        status=True)
        return render(requests, 'return.html',
                      {'message': "添加成功", 'href': "/studentinfo"})
    except Exception as e:
        print(e)
        return render(requests, 'return.html',
                      {'message': "添加失败，请检查输入", 'href': "/insertGoods"})

