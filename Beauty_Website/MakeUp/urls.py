"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from MakeUp import views
app_name="MakeUp"
urlpatterns = [
    path('', views.home, name='home'),
    path('sale',views.sale,name="sale"),
    path('cat/<n>',views.allcategories,name='allcategories'),
    path('allproduct/<p>',views.allproducts,name="allproducts"),
    path('detail/<p>',views.detail,name="detail"),
    path('userlogin',views.userlogin, name="userlogin"),
    path('register', views.register, name="register"),
    path('userlogout', views.userlogout, name="userlogout"),
    path('search', views.search, name='search'),

]
