"""pj07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from app01.views import index,showall,edit,page1,detail,page2,detail2,login2,page_admin2,logout2,edit2,del2,add2
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',index),
    re_path(r'^showall/$',showall),
    re_path(r'^edit/$',edit),
    re_path(r'^page1/$',page1),
    re_path(r'^detail/$',detail),
    re_path(r'^page2/$',page2),
    re_path(r'^detail2/$',detail2),
    re_path(r'^login2/$',login2),
    re_path(r'^page_admin2/$',page_admin2),
    re_path(r'^logout2/$',logout2),
    re_path(r'^edit2/$',edit2),
    re_path(r'^edit2/(\w+)/$',edit2),
    re_path(r'^del2/(\w+)/$',del2),
    re_path(r'^del2/$',del2),
    re_path(r'^add2/$',add2),
]
