from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_menu, name='menu_items')
]
