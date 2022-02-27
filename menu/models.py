from django.db import models

# Create your models here.

class Category(models.Model):
    ''' The different food categories '''
    class Meta:
        ''' How it appears in the admin '''
        verbose_name_plural = 'Service Categories'
    
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.get_friendly_name(self)