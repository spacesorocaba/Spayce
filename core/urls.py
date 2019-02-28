"""Spayce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from spayce.views import pedido, valeu, status, productlist, productview, \
    productdetail, productretrieve, orderlist, orderdetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pedido, name='principal'),
    path('thanks/', valeu, name='obrigado'),
    path('status/', status, name='status'),
    path('product/', productlist, name='product'),
    path('product/list/', productview, name='product-list-for-all-users'),
    path('product/<int:pk>/', productdetail, name='product-detail'),
    path('order/', orderlist, name='order'),
    path('order/<int:pk>/', orderdetail, name='order-detail')
    # path('product/get/<str:name>/', productretrieve,
    #      name='product-retrieve-for-all-users'),

]
