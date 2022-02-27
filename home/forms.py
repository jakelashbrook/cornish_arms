from django import forms 
from .models import Opening, Food


class OpeningForm(forms.Form):
    ''' A form to update the opening times '''
    model = Opening
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FoodForm(forms.Form):
    ''' A model to update the food times '''
    model = Food
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)