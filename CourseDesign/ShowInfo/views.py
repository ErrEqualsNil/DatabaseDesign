from django.shortcuts import render
from django.http import HttpResponseRedirect
from Model.models import Commodity, User, Transaction
# Create your views here.


def showInfo(requests):
    id = requests.GET.get('id')
    tmp = User.objects.filter(id=id)[0]
    datas = {'ID': id, 'Name': tmp.name, 'Sex': 'Male' if tmp.isMale else 'Female', 'College': tmp.college,
             'Address': tmp.address, 'QQ': tmp.QQ, 'Tel': tmp.tel, 'Email': tmp.email}
    good_list = Commodity.objects.filter(owner=id, status=True)
    Transaction1 = Transaction.objects.filter(seller = id)
    Trans = []
    for tra in Transaction1:
        Trans.append({'ID': tra.id, 'Name': tra.commodity.name, 'Price': tra.commodity.price, 'Seller': tra.seller,
                      'Comment': tra.comment,
                      'Buyer': requests.session['user'], 'Description': tra.commodity.description, 'Statue': tra.status,
                      'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(tra.commodity.image)})
    return render(requests, 'ShowInfo.html', {'datas': datas, 'goods': good_list, 'trans': Trans, 'len': len(good_list)})
