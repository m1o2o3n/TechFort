
from django.urls import path
from . import views as Portal_views

urlpatterns = {
    path('', Portal_views.GetList),
    path('article/<id>/', Portal_views.GetArticle),
    path('create/', Portal_views.CreateArticle),
}