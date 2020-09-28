from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Model.models import Commodity, Transaction, User
# Create your views here.

def itemInfo(request):
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
        'description': item.description
    }
    return render(request, 'itemInfo.html', itemInfos)

def finishPurchase(requests):
    buyer = requests.session['user']
    seller = requests.GET.get('sellerID')
    if buyer == seller:
        return render(requests, 'return.html',
                      {'message': "购买失败", 'href': "/search"})
    commodityID = requests.GET.get('id')
    status = 2
    try:
        commodity = Commodity.objects.filter(id=commodityID)[0]
        Transaction.objects.create(buyer=buyer, seller=seller,
                                   commodity=commodity,
                                   status=status)
        commodity.status = False
        commodity.save()
        return render(requests, 'return.html',
                      {'message': "购买成功,待卖家确认", 'href': "/search"})
    except Exception as e:
        print(e)
        return render(requests, 'return.html',
                      {'message': "购买失败", 'href': "/search"})