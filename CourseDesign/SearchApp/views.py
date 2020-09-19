from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Login.models import Commodity
# Create your views here.

def searchResult(request):
    searchKey = request.GET.get('searchKey')
    good_list = Commodity.objects.filter(name=searchKey)
    goods = []
    for good in good_list:
        goods.append({'ID': good.ID, 'Name': good.name, 'Price': good.price, 'Description': good.description})
    return render(request, 'SearchResult.html', {'goods': goods, 'len': len(goods)})


def searchPage(requests):
    return render(requests, 'Search.html')

