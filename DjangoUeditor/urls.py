# coding:utf-8
# from django.conf.urls import url
from django.urls import path

from .views import get_ueditor_controller

urlpatterns = [
    # url(r'^controller/$', get_ueditor_controller),
    path(r'controller/', get_ueditor_controller),
]
