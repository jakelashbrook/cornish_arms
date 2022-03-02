from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menu/menu.html', views.menu, name='menu')
]
