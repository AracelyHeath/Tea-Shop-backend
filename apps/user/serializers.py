from .models import User
from rest_framework import serializers 
import datetime
from secrets import token_hex
from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model=User
        fields=('name','email','password','token','token_expires')

class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token =  serializers.CharField(read_only=True)
    token_expires = serializers.DateTimeField(read_only=True)

    class Meta:
        model=User
        fields=('name','email','password','token','token_expires')
    
    def create(self, validated_data):
        #encrypt the password
        validated_data['password']= make_password(validated_data['password'])
        #create a token
        validated_data['token']= token_hex(30)
        validated_data['token_expires']=datetime.datetime.now()+datetime.timedelta(days=7)
        return super().create(validated_data)


class UserSignInSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    token_expires = serializers.DateTimeField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model=User
        fields=('name','email','password','token','token_expires')

    def create (self, validated_data):
        user=User.objects.filter(email=validated_data['email']) 
        #check the password
        if len(user)>0 and check_password(validated_data['password'], user[0].password):
            user[0].token=token_hex(30)
            user[0].token_expires=datetime.datetime.now()+datetime.timedelta(days=7) 
            user[0].save()
            return user[0] 
        else:
            raise seriaizers.ValidationError({'error':'The password or email is incorrect'})