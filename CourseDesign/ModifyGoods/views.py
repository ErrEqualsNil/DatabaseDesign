from django.shortcuts import render
from django.http import HttpResponseRedirect
from Model.models import Commodity
# Create your views here.


def modifyGoods(requests):
    id = requests.GET.get('id')
    tmp = Commodity.objects.filter(id=id)[0]
    datas = {'Name': tmp.name, 'Price': tmp.price, 'Description': tmp.description}
    return render(requests, 'ModifyGoods.html', {'datas': datas})


def modifyResult(requests):
    itemName = requests.POST.get('itemName')
    itemPrice = requests.POST.get('itemPrice')
    itemDescription = requests.POST.get('itemDescription')
    id = requests.GET.get('id')
    try:
        item = Commodity.objects.filter(id=id).update(name=itemName, price=itemPrice, description=itemDescription)
        return HttpResponseRedirect('/studentinfo')
    except Exception as e:
        return render(requests, 'return.html',
                      {'message': "修改失败，请检查输入", 'href': "/studentinfo"})