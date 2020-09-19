from django.shortcuts import render
import random

# Create your views here.


def Page(requests):
    data = []
    for i in range(1, 11):
        data.append({'id': i, 'name': "GOOD" + str(i), 'price': random.random, 'description': "none"})
    return render(requests, 'GoodsShowTest.html', {'datas': data})
