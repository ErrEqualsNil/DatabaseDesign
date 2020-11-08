from django.shortcuts import render, HttpResponseRedirect
from Model.models import Commodity, User, Transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import connection, transaction
import oss2

def OrderPage(requests):
    if 'user' not in requests.session:
        return HttpResponseRedirect("/login")
    tmp = User.objects.filter(id=requests.session['user'])[0]
    Transaction1 = Transaction.objects.filter(buyer=requests.session['user'])
    Commodity1 = Commodity.objects.filter(status=True)
    Trans = []
    for tra in Transaction1:
        Trans.append({'ID':tra.id, 'Name': tra.commodity.name, 'Price':tra.commodity.price, 'Seller':tra.seller,
                    'Buyer':requests.session['user'], 'Description':tra.commodity.description, 'Statue':tra.status,
                    'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(tra.commodity.image)})
    return render(requests, 'OrderCheck.html', {'Trans':Trans, 'len':len(Trans)})