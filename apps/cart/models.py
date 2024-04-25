from django.db import models
from apps.item.models import Item
from apps.user.models import User
# Create your models here.
class Cart(models.Model):
    class Meta(object):
        db_table='cart'

    user =models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    item =models.ForeignKey(Item, db_index=True, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity', blank=False, null=False)
    updated_at = models.DateTimeField('Updated_at',  blank=True, auto_now=True)
    created_at = models.DateTimeField('Created_at', blank=True, auto_now_add=True) 


    def __str__(self):
        return self.name