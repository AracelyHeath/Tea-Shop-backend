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


class UserList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer