from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *


def GetList(request):
    if request.method == 'GET':
        articles = Articles.objects.all()
        # print(articles[0])
        # response = json.dumps(articles[0])
        # return HttpResponse(response,  content_type='application/json;charset = utf-8', charset='utf-8')
        # 将model数据json返回

    return HttpResponse("使用get请求")


def GetArticle(request, id):
    if request.method == 'GET':

        return HttpResponse("文章详情" + id)
    return HttpResponse("使用get")


def GetTips(request):
    if request.method == 'GET':
        return HttpResponse("gettips")
    return HttpResponse("使用get")


def CreateArticle(request):
    if request.method == 'POST':
        title = request.POST['title']
        tips = request.POST['tips']
        content = request.POST['content']
        author = request.user

        if author == '':
            print(author)

        print(author.id)
        print(title + content)
        if author and title and content:
            print("用户信息通过")
            aritcle = Articles(title=title, author=author, tips=tips, content=content)
            aritcle.save()
            print("写入成功")
            return HttpResponse('写入完成')

        return HttpResponse("提交信息不全")
