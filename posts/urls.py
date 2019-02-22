from django.urls import path,re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('details/<id>', views.detail, name='detail'),
    path('addnew',views.add,name='add'),
    path('insert',csrf_exempt(views.insert),name='insert'),
    path('update/<id>', csrf_exempt(views.update), name='update'),
    path('delete/<id>', csrf_exempt(views.delete), name='delete'),
    re_path(r'[A-Za-z0-9_]+/', views.notfound, name='error')
];