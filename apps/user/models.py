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

    name = models.CharField('Name', max_length = 50, blank=False, null=False , db_index = True) 
    email = models.EmailField('Email', max_length = 50, blank=False, null=False, db_index = True)
    password = models.CharField('Password', max_length=50, blank=False, null=False, db_index = True)
    token = models.CharField('Token', max_length=500, blank=True, db_index=True)
    updated_at = models.DateTimeField('Update_at',  blank=True, auto_now=True)
    created_at = models.DateTimeField('Created_at', blank=True, auto_now_add=True)
    token_expires = models.DateTimeField('Token_expires', blank=True, null=True)


# JSON data -> javascript oject notation