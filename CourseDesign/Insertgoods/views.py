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
    key = 'LTAI4FzSxsT' + 'G9WmSi4UhykiP'
    password = 'FPI6XHyeybIF'+ 'ahASoJzQ30YBzd6yjK'
    auth = oss2.Auth(key, password)
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, 'database-design')
    itemImage = requests.FILES.get("itemImage")
    try:
        item = Commodity.objects.create(name=itemName, price=itemPrice,
                                description=itemDescription, owner=requests.session['user'],
                                status=True, image="0")
        res = bucket.put_object(str(item.id) + '-0.jpg', itemImage)
        print(itemImage)
        item.image = str(item.id) + '-0.jpg'
        item.save()
        return render(requests, 'return.html',
                      {'message': "添加成功", 'href': "/studentinfo"})
    except Exception as e:
        print(e)
        return render(requests, 'return.html',
                      {'message': "添加失败，请检查输入", 'href': "/insertGoods"})

