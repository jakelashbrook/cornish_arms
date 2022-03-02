from django.contrib import admin
from .models import Category, Dishes
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ''' Organises the Category Admin '''
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class DishesAdmin(admin.ModelAdmin):
    ''' Organises the Dishes Admin '''
    list_display = (
        'name', 'category_name',
        'price', 'description',
        'if_allergens', 'out_of_stock',
        'is_vegan', 'is_gluten_free',
        'image',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dishes, DishesAdmin)