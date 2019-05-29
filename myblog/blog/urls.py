from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # 首页
    path('', views.index, name='home'),
    # 列表页
    path('list/', views.list, name='list'),
    # 内容页
    path('show/', views.show, name='show'),
    # 标签页
    path('tag/', views.tag, name='tag'),
    # 搜索页
    path('search/', views.search, name='search'),
    # 联系我们单页
    path('about/', views.about, name='about'),
]