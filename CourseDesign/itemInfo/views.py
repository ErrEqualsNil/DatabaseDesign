from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Model.models import Commodity, Transaction, User
from django.db import transaction
# Create your views here.

def itemInfo(request):
    try:
        itemID = request.GET.get('id')
        item = Commodity.objects.filter(id=itemID)[0]
        ownerName = User.objects.filter(id=item.owner)[0].name
        itemInfos = {
            'ID': item.id,
            'name': item.name,
            'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + item.image,
            'ownerID': item.owner,
            'ownerName': ownerName,
            'price': item.price,
            'description': item.description,
            'status': int(item.status)
        }
        if 'user' not in request.session:
            itemInfos['status'] = 3  # 用户未登录，隐藏购买按钮
        return render(request, 'itemInfo.html', itemInfos)
    except Exception as e:
        print(e)
        return render(request, 'return.html',
                      {'message': '暂无该商品信息', 'href': "/search"})

def finishPurchase(requests):
    buyer = requests.session['user']
    seller = requests.GET.get('sellerID')
    if buyer == seller:
        return render(requests, 'return.html',
                      {'message': "购买失败", 'href': "/search"})
    commodityID = requests.GET.get('id')
    status = 2
    try:
        with transaction.atomic():
            commodity = Commodity.objects.filter(id=commodityID)[0]
            if commodity.status == True:
                Transaction.objects.create(buyer=buyer, seller=seller,
                                           commodity=commodity,
                                           status=status)
                commodity.status = False
                commodity.save()
                return render(requests, 'return.html',
                              {'message': "购买成功,待卖家确认", 'href': "/search"})
            else:
                raise Exception("手慢了 该商品已被购买！")
    except Exception as e:
        return render(requests, 'return.html',
                      {'message': e, 'href': "/search"})

