from django.conf.urls import include, url
from django.contrib import admin

from app01 import views

# index
urlpatterns = [

    # http://127.0.0.1:8080/app01/index
    # 参数1: 匹配url的正则表达式
    # 参数2: 匹配成功后执行的视图函数
    url(r'^index$', views.index),

    # # http://127.0.0.1:8080/show_deps
    # url(r'^show_deps$', views.show_deps),
    #
    # # http://127.0.0.1:8000/show_dep/部门id
    # url(r'^show_dep/(\d+)$', views.show_dep),
]
