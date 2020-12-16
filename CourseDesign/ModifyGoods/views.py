from django.shortcuts import render
from django.http import HttpResponseRedirect
from Model.models import Commodity
# Create your views here.
import oss2


def modifyGoods(requests):
    id = requests.GET.get('id')
    tmp = Commodity.objects.filter(id=id)[0]
    datas = {'ID': id, 'Name': tmp.name, 'Price': tmp.price, 'Description': tmp.description, 'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(tmp.image)}
    return render(requests, 'ModifyGoods.html', {'datas': datas})


def modifyResult(requests):
    itemName = requests.POST.get('itemName')
    itemPrice = requests.POST.get('itemPrice')
    itemDescription = requests.POST.get('itemDescription')
    id = requests.GET.get('id')
    key = 'LTA'+'I4GF'+'kNx'
    key = key + 'HzH'+'ejr7'+'Xj8'+'da9o'
    password = 'QXR'+'i6uKVthP'+'xInBRVScB413'+'JW5rHxi'
    auth = oss2.Auth(key, password)
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, 'database-design')
    itemImage = requests.FILES.get("itemImage")
    try:
        Commodity.objects.filter(id=id).update(name=itemName, price=itemPrice, description=itemDescription)
        item = Commodity.objects.filter(id=id)[0]
        if itemImage is not None:
            bucket.delete_object(str(item.image))
            print(item.image)
            if str(item.image)[-5] == '0':
                bucket.put_object(str(id) + '-1.jpg', itemImage)
                item.image = str(id) + '-1.jpg'
            else:
                bucket.put_object(str(id) + '-0.jpg', itemImage)
                item.image = str(id) + '-0.jpg'
        item.save()
        return HttpResponseRedirect('/studentinfo')
    except Exception as e:
        print(e)
        return render(requests, 'return.html',
                      {'message': "修改失败，请检查输入", 'href': "/studentinfo"})