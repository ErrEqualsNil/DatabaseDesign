from django.shortcuts import render, HttpResponseRedirect
from Model.models import Commodity, User, Transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import connection, transaction
import oss2

def CommentPage(requests):
    if 'user' not in requests.session:
        return HttpResponseRedirect("/login")
    id = requests.GET.get('id')
    tmp = Transaction.objects.filter(id=id)[0]
    datas = {'ID': id, 'Comment': tmp.comment}
    return render(requests, 'ModifyComment.html', {'datas': datas})
def commentResult(requests):
    transComment = requests.POST.get('transComment')
    id = requests.GET.get('id')
    key = 'LTAI4FzSxsT' + 'G9WmSi4UhykiP'
    password = 'FPI6XHyeybIF'+ 'ahASoJzQ30YBzd6yjK'
    auth = oss2.Auth(key, password)
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, 'database-design')
    try:
        Transaction.objects.filter(id=id).update(comment=transComment)
        return HttpResponseRedirect('/studentinfo')
    except Exception as e:
        print(e)
        return render(requests, 'return.html',
                      {'message': "修改失败，请检查输入", 'href': "/studentinfo"})
