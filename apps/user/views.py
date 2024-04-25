from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSignInSerializer, UserSignUpSerializer, UserSerializer
from .models import User
import re
from .mixins import CustomLoginRequiredMixin
# Create your views here.
class UserSignUp(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSignUpSerializer 

class UserSignIn(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSignInSerializer

class UserCheckLogin(CustomLoginRequiredMixin, generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        serializer=UserSerializer([request.login_user], many=True) 
        return response(serializer.data[0])       

class UserList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


#biryani 