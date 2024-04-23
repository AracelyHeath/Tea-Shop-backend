from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Item(models.Model):
    class Meta(object):
        db_table='item'

    name = models.CharField('Name', max_length= 50, blank=False, null=False , db_index=True) 
    price = models.DecimalField('Price', blank=False, null=False, max_digits=15, decimal_places=2)   
    image = CloudinaryField('Image', blank=False, null=False)
    updated_at = models.DateTimeField('Updated_at',  blank=True, auto_now=True)
    created_at = models.DateTimeField('Created_at', blank=True, auto_now_add=True) 


    def __str__(self):
        return self.name