from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Model.models import Commodity
# Create your views here.

def searchResult(request):
    searchKey = request.GET.get('searchKey')
    good_list = Commodity.objects.filter(name__icontains=searchKey, status=True)
    goods = []
    for good in good_list:
        goods.append({'ID': good.id, 'Name': good.name, 'Price': good.price,
                      'Description': good.description, 'Owner': good.owner,
                      'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(good.id) + ".jpg"})
    return render(request, 'SearchResult.html', {'goods': goods, 'len': len(goods), 'key': searchKey})


def searchPage(requests):
    return render(requests, 'Search.html')

