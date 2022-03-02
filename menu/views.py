from django.shortcuts import render
from .models import Category, Dishes
from .forms import MenuForm
# Create your views here.

def get_menu(request):
    ''' A view to return all the menu items, and sort/search through the items  '''
    dishes = Dishes.objects.all()

    template = 'menu/menu.html'
    context = {
        'dishes': dishes,
    }
  
    return render(request, template, context)