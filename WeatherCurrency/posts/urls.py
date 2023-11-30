from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', pages),
    path('<int:id>', page),
    path('add', create_article_page),
]
