from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
from .models import *
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# 获取文章列表
def GetList(request):
    if request.method == 'GET':
        articles = Articles.objects.all()
        res = serializers.serialize('json', articles)
        # print(articles[0])
        # response = json.dumps(articles[0])
        return HttpResponse(res,  content_type='application/json;charset = utf-8', charset='utf-8')
        # 将model数据json返回

    return HttpResponse("使用get请求")


# 获取文章
def GetArticle(request, id = '1'):
    # id = id
    id = request.GET['id']
    if id == '':
        return HttpResponse("没有参数")
    # if request.method == 'GET':
    article = Articles.objects.get(id='1')
    return HttpResponse(serializers.serialize('json', article), content_type='application/json;charset = uft-8', charset='utf-8')
    # return Http404


# 获取标签
def GetTips(request):
    if request.method == 'GET':
        return HttpResponse("gettips")
    return HttpResponse("使用get")


# 创建文章
def CreateArticle(request):
    if request.method == 'POST':
        title = request.POST['title']
        tips = request.POST['tips']
        content = request.POST['content']
        author = request.user
        if author == '':
            return Http404
        if author and title and content:
            # print("用户信息通过")
            aritcle = Articles(title=title, author=author, tips=tips, content=content)
            aritcle.save()
            # print("写入成功")
            return HttpResponse('写入完成')

        return Http404


# 目前只提供标题搜索
def SearchAritcle(request):
    if request.method ==  'POST':
        key = request.POST['key']
        res = Articles.objects.filter(title_icontains = key)
        return HttpResponse(serializers.serialize('json', res), content_type='application/json;charset = utf-8', charset='utf-8')


# 根据用户id获取文章
def GetArticlebyId(request):
    if request.method == 'POST':
        if request.POST['searchUserId'] == '':
            return Http404
        searchUserId = request.POST['searchUserId']
        user = User.objects.get(id = searchUserId)
        res = Articles.objects.filter(author = user).all()
        return HttpResponse(serializers.serialize('json', res), content_type='application/json;charset = uft-8', charset='utf-8')