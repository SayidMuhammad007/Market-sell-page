from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Main, name='main'),
    path('sell/<id>', Amount_page, name='amount_page')
]
