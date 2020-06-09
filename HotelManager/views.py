from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import time
import random


# Create your views here.
def roomPost(request):
    # context2 = {'parameter1': "参数4", 'parameter2': "参数5", 'parameter3': "参数6"}
    # context = {'parameter1': "参数1", 'parameter2': "参数2", 'parameter3': "参数3"}
    context = {}
    context['refresh'] = 3
    context['parameter1'] = random.random
    context['parameter2'] = random.random
    context['parameter3'] = random.random
    return render(request, 'HotelPost.html', context)


def queryPost(request):
    room_num = request.GET['room_number']
    print(room_num)

    return HttpResponseRedirect('/HotelManager/roomPost')


def setPrice(request):
    pri = request.GET['price']
    print(pri)
    context = {'result_price': '设置成功'}
    return render(request, 'HotelManagerWel.html', context)


def setTemp(request):
    temp = request.GET['tempreture']
    print(temp)
    context = {'result_temp': '设置成功'}
    return render(request, 'HotelManagerWel.html', context)


def welcome(request):
    return render(request, 'HotelManagerWel.html')
