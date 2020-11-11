from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Model.models import Commodity, Transaction
# Create your views here.

def searchResult(request):
    searchKey = request.GET.get('searchKey')
    keys = searchKey.split(' ')
    goods = []
    good_list = Commodity.objects.filter(name__icontains=keys[0], status=True)
    for key in keys[1:]:
        good_list = good_list.filter(name__icontains=key, status=True)
    for good in good_list:
        goods.append({'ID': good.id, 'Name': good.name, 'Price': good.price,
                    'Description': good.description, 'Owner': good.owner,
                    'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(good.image)})
    if 'user' in request.session:
        sellConfirm = Transaction.objects.filter(seller=request.session['user'], status=2)
        request.session['message'] = len(sellConfirm)
    return render(request, 'SearchResult.html', {'goods': goods, 'len': len(goods), 'key': searchKey})


def searchPage(requests):
    return render(requests, 'Search.html')

