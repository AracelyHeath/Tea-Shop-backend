from django.db import models

# Create your models here.
class Cart(models.Model):
    class Meta(object):
        db_table='cart'

    user =models.ForeignKey('User',)
    item =models.ForeignKey('Item')
    quantity = models.IntegerField('Quantity',blank=False, null=False, max_digits=3)
     updated_at = models.DateTimeField('Updated_at',  blank=True, auto_now=True)
    created_at = models.DateTimeField('Created_at', blank=True, auto_now_add=True) 


    def __str__(self):
        return self.name