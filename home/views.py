from django.shortcuts import render
from .models import Opening, Food, About


# Create your views here.
def index(request):
    ''' A view to return the index page '''
    opening = Opening.objects.all()
    food = Food.objects.all()
    about = About.objects.all()

    template = 'home/index.html'
    context = {
        'opening': opening,
        'food': food,
        'about': about,
    }


    return render(request, template, context)
