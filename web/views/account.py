# 和用户账户相关的功能：注册、短信、登录、注销
from django.shortcuts import render


def register(request):
    return render(request, 'register.html')
