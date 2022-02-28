from django.db import models


class Opening(models.Model):
    ''' A model for the opening times '''
    class Meta:
        verbose_name_plural = 'Opening Times'
    model_name = models.Charfield(max_length=40)
    monday = models.CharField(max_length=50, default='timezone.now')
    tuesday = models.CharField(max_length=50, default='timezone.now')
    wednesday = models.CharField(max_length=50, default='timezone.now')
    thursday = models.CharField(max_length=50, default='timezone.now')
    friday = models.CharField(max_length=50, default='timezone.now')
    saturday = models.CharField(max_length=50, default='timezone.now')
    sunday = models.CharField(max_length=50, default='timezone.now')

    def __str__(self):
        return self.model_name


class Food(models.Model):
    ''' The food service hours '''

    class Meta:
        verbose_name_plural = 'Food Times'
    model_name = models.CharField(max_length=30)
    monday = models.CharField(max_length=50, default='timezone.now')
    tuesday = models.CharField(max_length=50, default='timezone.now')
    wednesday = models.CharField(max_length=50, default='timezone.now')
    thursday = models.CharField(max_length=50, default='timezone.now')
    friday = models.CharField(max_length=50, default='timezone.now')
    saturday = models.CharField(max_length=50, default='timezone.now')
    sunday = models.CharField(max_length=50, default='timezone.now')
    if_lunch = models.BooleanField(default=False)
    lunch_hours = models.CharField(max_length=50, default='timezone.now')

    def __str__(self):
        return self.model_name


class About(models.Model):
    ''' A model to edit the About Us Section '''
    class Meta:
        ''' Sets the name in the admin '''
        verbose_name_plural = 'About Us'
    model_name = models.CharField(max_length=20)
    title = models.CharField(max_length=60, blank=False, null=False)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    background_image = models.ImageField(
        upload_to='media/', height_field=None, 
        width_field=None, max_length=100)
    
    def __str__(self):
        return self.model_name