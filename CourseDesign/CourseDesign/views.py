from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect

def startPage(requests):
    if 'type' not in requests.session:
        return HttpResponseRedirect("/search")
    elif requests.session['type'] == 'student':
        return HttpResponseRedirect("/search")
    else:
        return HttpResponseRedirect("/teachers")

