from django.db import models

# Create your models here.
# models -> module
# Model -> class
# Model is the parent class
# User is the child class
#inheritance
class User(models.Model):
    class Meta(object):
        db_table = 'user'

    name = models.CharField('Name', max_length = 50, blank=False, null=False) 
    created_at = models.DateTimeField('Created_at', blank=True, auto_now_add=True)