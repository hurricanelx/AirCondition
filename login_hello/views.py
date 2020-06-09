from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from login_hello.models import User, AirC
from django.contrib import auth

# Create your views here.


def login_(request):
    return HttpResponseRedirect('/login/')


def register_(request):
    return HttpResponseRedirect('/register/')


def login_welcome(request):
    return render(request, 'login_welcome.html')


def register_welcome(request):
    return render(request, 'register_welcome.html')


def login(request):
    username = request.GET['name']
    pwd = request.GET['password']
    print(username)
    print(pwd)
    user = User.objects.filter(user_name=username, password=pwd)
    if user:
        user = user[0]
        if user.user_type == 'C':
            return HttpResponseRedirect('/Customer/')
        elif user.user_type == 'A':
            return HttpResponseRedirect('/AirConManager/')
        elif user.user_type == 'H':
            return HttpResponseRedirect('/HotelManager/')

    else:
        context = {}
        context['result'] = '用户名或密码错误。'
        return render(request, 'login_welcome.html', context)


def register(request):
    username = request.GET['name']
    pwd = request.GET['password']
    user_type = request.GET['user_type']

    temp_user = User.objects.filter(user_name=username, password=pwd)
    if temp_user:
        User.objects.filter(user_name=username).update(user_type=user_type)
        context = {}
        context['result'] = '修改用户类型成功'
        return render(request, 'register_welcome.html', context)
    else:
        user = User.objects.create(user_name=username, password=pwd, user_type=user_type)
        if user:
            print(user)
            context = {}
            context['result'] = '添加成功'
            return render(request, 'register_welcome.html', context)
        else:
            context = {}
            context['result'] = '添加失败'
            return render(request, 'register_welcome.html', context)



def welcome(request):
    return render(request, 'hello.html')
