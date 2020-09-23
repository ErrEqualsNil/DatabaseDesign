from django.shortcuts import render
from django.http import HttpResponseRedirect
from Model.models import Commodity
from django.contrib import messages
# Create your views here.
import oss2

def insertGoodsPage(requests):
    return render(requests, 'insertGoods.html')


def insertGoodsResult(requests):
    itemName = requests.POST.get('itemName')
    itemPrice = requests.POST.get('itemPrice')
    itemDescription = requests.POST.get('itemDescription')

    auth = oss2.Auth('LTAI4FzSxsTG9WmSi4UhykiP', 'FPI6XHyeybIFahASoJzQ30YBzd6yjK')
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, 'database-design')
    itemImage = requests.FILES.get("itemImage")
    bucket.put_object()

    try:
        item = Commodity.objects.create(id=,name=itemName, price=itemPrice,
                                description=itemDescription, owner=requests.session['user'],
                                status=True)
        return render(requests, 'return.html',
                      {'message': "添加成功", 'href': "/studentinfo"})
    except Exception as e:
        print(e)
        return render(requests, 'return.html',
                      {'message': "添加失败，请检查输入", 'href': "/insertGoods"})

