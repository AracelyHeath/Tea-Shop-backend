from django.db import models
from apps.item.models import Item
from apps.user.models import User
from apps.user.models import Cart

# Create your models here.
class Order(models.Model):
    class Meta(object):
        db_table='order'

    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    total_price = models.DecimalField('Total_Price', blank=False, null=False, max_digits=15, decimal_places=2)
    full_name = models.CharField('Full_Name', max_length= 50, blank=False, null=False , db_index=True)
    address_line1 = models.CharField('Address_line1', max_length= 50, blank=False, null=False , db_index=True)
    address_line2 = models.CharField('Address_line2', max_length= 50, blank=False, null=False , db_index=True)
    city =models.CharField('City', max_length= 50, blank=False, null=False , db_index=True)
    state =models.CharField('State', max_length= 50, blank=False, null=False , db_index=True)
    postal_code= models.IntegerField('Postal_code', blank=False, null=False)
    country = ('Country', max_length= 50, blank=False, null=False , db_index=True)
    telephone = models.IntegerField('Telephone', blank=False, null=False)
    updated_at = models.DateTimeField('Updated_at',  blank=True, auto_now=True)
    created_at = models.DateTimeField('Created_at', blank=True, auto_now_add=True)    


class OrderItem(models.Model):
    class Meta(object):
        db_table'order_item'

    order = models.ForeignKey(Order, )
    item =models.ForeignKey(Item, db_index=True, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity', blank=False, null=False)
    updated_at = models.DateTimeField('Updated_at',  blank=True, auto_now=True)
    created_at = models.DateTimeField('Created_at', blank=True, auto_now_add=True)    



    def __str__(self):
        return self.name    