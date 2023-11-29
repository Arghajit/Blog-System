from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home),
    path('main/',views.main,name="main"),
    path('new/',views.new,name="new"),
    path('login/',views.login,name="login"),
    path('addblog/',views.addblog,name="addblog"),
    path('viewblog/',views.viewblog,name="viewblog"),
    path('upload/',views.upload,name="upload"),
]
