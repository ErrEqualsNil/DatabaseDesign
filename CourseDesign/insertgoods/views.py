from django.shortcuts import render
from Login.models import Commodity
from django.contrib import messages
# Create your views here.


def insertGoodsPage(requests):
    return render(requests, 'insertGoods.html')

def insertGoodsResult(requests):
    itemName = requests.GET.get('itemName')
    itemPrice = requests.GET.get('itemPrice')
    itemDescription = requests.GET.get('itemDescription')
    try:
        item = Commodity.objects.create(name=itemName, price=itemPrice,
                         description=itemDescription, owner=requests.session['user'])
        return render(requests, 'return.html',
                      {'message': "添加成功", 'href': "/studentinfo"})
    except Exception as e:
        print(e)
        return render(requests, 'return.html',
                      {'message': "添加失败，请检查输入", 'href': "/insertGoods"})

