from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Model.models import Commodity
# Create your views here.

def itemInfo(request):
    itemID = request.GET.get('id')
    item = Commodity.objects.filter(id=itemID)[0]
    itemInfos = {
        'name': item.name,
        'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + item.image,
        'owner': item.owner,
        'price': item.price,
        'description': item.description
    }
    return render(request, 'itemInfo.html', itemInfos)

