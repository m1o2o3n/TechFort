
from django.urls import path
from . import views as Portal_views

urlpatterns = {
    path('', Portal_views.GetList),
    path('arti/', Portal_views.GetArticle),
    path('create/', Portal_views.CreateArticle),
    path('getbyid/', Portal_views.GetArticlebyId),
    path('search/', Portal_views.SearchAritcle),
}