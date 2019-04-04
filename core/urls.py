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

from spayce.views import productlist, productview, \
    productdetail, orderlist, orderdetail, import_csv, spacerview, \
    import_products_csv, export_csv, spacerdetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export_csv/', export_csv, name='export_csv'),
    path('import_csv/', import_csv, name='import_csv'),
    path('import_products/', import_products_csv, name='import_csv'),
    path('api/spacers/', spacerview, name='spacers'),
    path('api/spacers/<int:cpf>/', spacerdetail, name='spacer'),
    path('api/products/', productlist, name='products'),
    path('api/products/list/', productview, name='product-list-for-all-users'),
    path('api/products/<int:pk>/', productdetail, name='product-detail'),
    path('api/orders/', orderlist, name='orders'),
    path('api/orders/<int:pk>/', orderdetail, name='order-detail')
]
