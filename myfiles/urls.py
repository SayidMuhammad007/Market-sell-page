from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Main, name='main'),
    path('sell/<id>', Amount_page, name='amount_page'),
    path('sell_page/', Sell_page, name='sell_page'),
    path('sell_delete/<id>/', Sell_delete, name='sell_delete')
]
