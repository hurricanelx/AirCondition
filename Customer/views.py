from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
# Create your views here.


# @login_required
def welcome(request):
    user_name = request.session.get('user_name', False)
    if user_name:
        temp = random.random()
        context = {'room_number': temp}
        return render(request, 'CustomerWel.html', context)


def editCon(request):
    status = request.GET['switch']
    print(status)
    return render(request, 'CustomerWel.html')


def setTemp(request):
    temp = request.GET['tempreture']
    print(temp)
    context = {'result_temp': '设置成功', 'room_number':random.random()}
    return render(request, 'CustomerWel.html', context)


def setWind(request):
    wind = request.GET['windSpeed']
    print(wind)
    context = {'result_wind': '设置成功'}
    return render(request, 'CustomerWel.html', context)


def setMode(request):
    mode = request.GET['mode']
    print(mode)
    context = {'result_mode': '设置成功'}
    return render(request, 'CustomerWel.html', context)


def queryPost(request):
    context = {}
    context['user_id'] = ''
    context['user_name'] = ''
    context['energy'] = ''
    context['time'] = ''
    context['price'] = ''
    return render(request, 'CustomerPost.html')
