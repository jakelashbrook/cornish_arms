from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Dishes
from .forms import MenuForm
# Create your views here.

def menu(request):
    ''' A view to return the menu '''
    dishes = Dishes.objects.all()
    category = Category.objects.all()

    template = 'menu/menu.html'
    context = {
        'dishes': dishes,
        'category': category,
    }
  
    return render(request, template, context)