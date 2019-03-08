from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('registernewuser',csrf_exempt(views.registernewuser),name='registernewuser'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('posts',views.home,name='userhome'),
    path('logout',views.logout,name='logout'),
];