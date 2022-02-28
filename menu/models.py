from django.db import models

# Create your models here.

class Category(models.Model):
    ''' The different food categories '''
    class Meta:
        ''' How it appears in the admin '''
        verbose_name_plural = 'Service Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.get_friendly_name(self)


class Dishes(models.Model):
    ''' The menu dishes model '''
    class Meta:
        ''' Set name in django admin '''
        verbose_name_plural = 'Dishes'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=300)
    description = models.TextField()
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    out_of_stock = models.BooleanField(default=False)
    if_allergens = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name