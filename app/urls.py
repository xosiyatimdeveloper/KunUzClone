from django.contrib import admin
from django.urls import path, include
from .views import news_list, news_detail, home_page

urlpatterns = [
    path('',home_page, name='news_list'),
    path("news/<int:id>/", news_detail, name='news_detail_page')
]