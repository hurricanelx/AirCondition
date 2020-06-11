from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.http import HttpResponse, HttpResponseRedirect
import time
import random
from login_hello.models import User


# Create your views here.
def roomPost(request):
    # context2 = {'parameter1': "参数4", 'parameter2': "参数5", 'parameter3': "参数6"}
    # context = {'parameter1': "参数1", 'parameter2': "参数2", 'parameter3': "参数3"}
    context = {}
    context['refresh'] = 3
    if random.random() < 0.5:
        context['img_path'] = '../static/img/room.png'
    else:
        context['img_path'] = '../static/img/user.png'
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
    return redirect(reverse("data"))
    # return render(request, 'temp_hotel.html')


def data(request):
    post_list = User.objects.all()  # 直接提取需要的数据
    if post_list.exists() != 0:
        pag = Paginator(post_list, 3)
        page = request.GET.get('page')
        page = pag.get_page(page)
        return render(request, 'temp_hotel.html', {'u': page, 'name': 'temp'})
