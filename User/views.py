from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import auth,User

# Create your views here.


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponse("登录成功")
        print(request)
        return HttpResponse("用户名密码错误" + username + password)
    return HttpResponse("显示登陆页面")


def Logout(request):
    if request.method == 'POST':
        auth.login(request)
        return HttpResponse("注销成功")


def Reg(request):
    username = request.POST['username']
    password = request.POST['password']
    user_info = User.objects.create_user(username=username, password=password)
    return HttpResponse("注册成功")


def Set_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        newpassword = request.POST['newpassword']
        user = auth.authenticate(username=username, password=password)
        if user:
            user.set_password(password=newpassword)
            user.save()
            return HttpResponse("修改成功")
