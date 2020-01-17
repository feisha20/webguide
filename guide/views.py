from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from guide import models
from guide.models import Titles
from guide.models import Urls
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os


# 栏目列表
@login_required
def titles(request):
    titles = Titles.objects.all()
    return render(request, "titles.html", {"titles": titles})


# 新增栏目
@login_required
def add_title(request):
    if request.method == 'GET':
        return render(request, 'add_title.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        is_main = request.POST.get('is_main')
        sort = request.POST.get('sort')
        sub_title_num = Titles.objects.filter(is_main=0).count()
        if sub_title_num >= 3:
            messages.success(request, "最多只能添加3个子栏目")
            return render(request, "add_title.html")
        else:
            models.Titles.objects.create(
                title=title,
                is_main=is_main,
                sort=sort
            )
        titles = Titles.objects.all()
        return render(request, "titles.html", {"titles": titles})


# 编辑栏目
@login_required
def edit_title(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        titles = models.Titles.objects.filter(id=nid).first()
        return render(request, 'edit_title.html', {'titles': titles})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        is_main = request.POST.get('is_main')
        sort = request.POST.get('sort')
        models.Titles.objects.filter(id=nid).update(
            title=title,
            is_main=is_main,
            sort=sort,
        )
        titles = Titles.objects.all()
        return render(request, "titles.html", {"titles": titles})


# 删除栏目
@login_required
def del_title(request):
    nid = request.GET.get('nid')
    models.Titles.objects.filter(id=nid).delete()
    titles = Titles.objects.all()
    return render(request, "titles.html", {"titles": titles})


# 网址列表
@login_required
def urls(request):
    urls = Urls.objects.values('id', 'title__title', 'name', 'url', 'logo', 'sort', 'update_time')
    return render(request, "urls.html", {"urls": urls})


# 新增网址
@login_required
def add_url(request):
    if request.method == 'GET':
        titles = Titles.objects.filter(is_main=0)
        return render(request, 'add_url.html', {"titles": titles})
    elif request.method == 'POST':
        title_id = request.POST.get('title_id')
        name = request.POST.get('name')
        url = request.POST.get('url')
        sort = request.POST.get('sort')
        myfile = request.FILES.get("logo")
        models.Urls.objects.create(
            title_id=title_id,
            name=name,
            url=url,
            logo=myfile,
            sort=sort
        )
    urls = Urls.objects.values('id', 'title__title', 'name', 'url', 'logo', 'sort', 'update_time')
    return render(request, "urls.html", {"urls": urls})


# 编辑网址
@login_required
def edit_url(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        titles = Titles.objects.filter(is_main=0)
        urls = models.Urls.objects.filter(id=nid).first()
        return render(request, 'edit_url.html', {'urls': urls, "titles": titles})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title_id = request.POST.get('title_id')
        name = request.POST.get('name')
        url = request.POST.get('url')
        # myfile = request.FILES.get("logo")
        sort = request.POST.get('sort')
        models.Urls.objects.filter(id=nid).update(
            title_id=title_id,
            name=name,
            url=url,
            # logo=myfile,
            sort=sort
        )
        urls = Urls.objects.values('id', 'title__title', 'name', 'url', 'logo', 'sort', 'update_time')
        return render(request, "urls.html", {"urls": urls})


# 删除网址
@login_required
def del_url(request):
    nid = request.GET.get('nid')
    models.Urls.objects.filter(id=nid).delete()
    urls = Urls.objects.values('id', 'title__title', 'name', 'url', 'logo', 'sort', 'update_time')
    return render(request, "urls.html", {"urls": urls})
