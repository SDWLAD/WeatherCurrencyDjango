from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('translator/', translator),
    path('weather/', weather),
    path('currency/', currency),
    
    path('currency/convert/', convert),
]
