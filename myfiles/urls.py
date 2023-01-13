from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Main, name='main'),
    path('sell/<id>', Amount_page, name='amount_page'),
    path('sell_page/', Sell_page, name='sell_page'),
    path('sell_delete/<id>/', Sell_delete, name='sell_delete'),
    path('sell_price/<id>/', Sell_price, name='sell_price'),
    path('selled/<type>', Selled, name='selled'),
    path('nasiya', Customer_page, name='customer_page'),
    path('nasiya/add', Customer_add, name='customer_add')
]
