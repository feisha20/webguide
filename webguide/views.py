from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from guide import models
from guide.models import Titles
from guide.models import Urls
from django.contrib.auth.decorators import login_required


# 登录
def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': '账号或者密码错误，请重新输入！'})
    return render(request, 'login.html')


# 后台首页
@login_required
def home(request):
    return render(request, "home.html")


# 首页
def index(request):
    main_title = Titles.objects.filter(is_main=1).order_by('-id')
    sub_titles = Titles.objects.filter(is_main=0).order_by('sort')
    sub_titles_num = Titles.objects.filter(is_main=0).count()
    if sub_titles_num == 1:
        urls1 = Urls.objects.filter(title=sub_titles.first().id).order_by('sort')
        return render(request, "index.html",
                      {"main_title": main_title, "sub_titles": sub_titles, "urls": urls1})
    elif sub_titles_num == 2:
        urls1 = Urls.objects.filter(title=sub_titles.first().id).order_by('sort')
        urls2 = Urls.objects.filter(title=sub_titles[1].id).order_by('sort')
        return render(request, "index.html",
                      {"main_title": main_title, "sub_titles": sub_titles, "urls": urls1, "urls2": urls2})
    elif sub_titles_num == 3:
        urls1 = Urls.objects.filter(title=sub_titles.first().id).order_by('sort')
        urls2 = Urls.objects.filter(title=sub_titles[1].id).order_by('sort')
        urls3 = Urls.objects.filter(title=sub_titles[2].id).order_by('sort')
        return render(request, "index.html",
                      {"main_title": main_title, "sub_titles": sub_titles, "urls": urls1, "urls2": urls2,
                       "urls3": urls3})
    else:
        return render(request, "index.html",
                      {"main_title": main_title, "sub_titles": sub_titles})


# 登出
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
