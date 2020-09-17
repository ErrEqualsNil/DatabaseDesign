from django.shortcuts import render, HttpResponse

# Create your views here.

def searchResult(requests):
    searchKey = requests.GET.get('searchKey')
    return HttpResponse(searchKey)

def searchPage(requests):
    return render(requests, 'Search.html')