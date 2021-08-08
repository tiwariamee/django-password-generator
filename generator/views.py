from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def password(request):
    thepassword = 'testing'
    charachters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('Length', 12))
    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        charachters.extend(list('!^%&#$(!*#$)'))
    if request.GET.get('Numbers'):
        charachters.extend(list('123456789'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charachters)

    return render(request, 'generator/password.html', {'password': thepassword})


def home(request):
    thepassword = 'testing'
    return render(request, 'generator/home.html', {'password': 'thepassword'})
