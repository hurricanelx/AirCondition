from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def editCon(request):
    status = request.GET['switch']
    print(status)
    return render(request, 'AirConManagerWel.html')


def welcome(request):
    user_name = request.session.get('user_name', False)
    if user_name:
        return render(request, 'AirConManagerWel.html')


# @login_required
def set_(request):
    user_name = request.session.get('user_name', False)
    if user_name:
        return render(request, 'AirConManSet.html')


def setPrice(request):
    user_id = request.GET['name']
    pri = request.GET['price']
    print(user_id, pri)
    context = {'result_price': '设置成功'}
    return render(request, 'AirConManSet.html', context)


def setTemp(request):
    user_id = request.GET['name']
    temp = request.GET['tempreture']
    print(user_id, temp)
    context = {'result_temp': '设置成功'}
    return render(request, 'AirConManSet.html', context)


def setMode(request):
    user_id = request.GET['name']
    mode = request.GET['mode']
    print(user_id, mode)
    context = {'result_mode': '设置成功'}
    return render(request, 'AirConManSet.html', context)


def setFrequency(request):
    user_id = request.GET['name']
    frequency = request.GET['frequency']
    print(user_id, frequency)
    context = {'result_frequency': '设置成功'}
    return render(request, 'AirConManSet.html', context)
