from django.shortcuts import render, HttpResponseRedirect
from Model.models import Commodity, User
from django.contrib import messages
from django.http import HttpResponseRedirect
import oss2

# Create your views here.
def InfoPage(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
    tmp = User.objects.filter(id=request.session['user'])[0]
    datas = {'Account': request.session['user'], 'Name': tmp.name,
             'Birthday': tmp.birthday, 'Sex': 'Male' if tmp.isMale else 'Female',
             'College': tmp.college, 'Address': tmp.address,
             'QQ': tmp.QQ, 'Telephone': tmp.tel,
             'Email': tmp.email}
    good_list = Commodity.objects.filter(owner=request.session['user'], status=True)
    goods = []
    for good in good_list:
        goods.append({'ID': good.id, 'Name': good.name, 'Price': good.price, 'Description': good.description,
                      'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(good.image)})
    return render(request, 'StudentInfo.html', {'datas': datas, 'goods': goods, 'len': len(goods), 'messageNum': 0})


def DeleteItem(request):
    delete_list = request.POST.getlist('choose')
    key = 'LTAI4FzSxsTG9WmSi4UhykiP'
    password = 'FPI6XHyeybIFahASoJzQ30YBzd6yjK'
    auth = oss2.Auth(key, password)
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, 'database-design')
    for Id in delete_list:
        bucket.delete_object(str(Commodity.objects.filter(id=Id)[0].image))
        Commodity.objects.filter(id=Id).delete()
    return HttpResponseRedirect('/studentinfo')
