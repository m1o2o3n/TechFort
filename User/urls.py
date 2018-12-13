from django.urls import path
from . import views as User_views

urlpatterns = [

    path('login/', User_views.Login),
    path('reg/', User_views.Reg),
    path('logout/', User_views.Logout),
    path('setpwd/', User_views.Set_password)
]