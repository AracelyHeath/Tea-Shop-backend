from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
# Create your views here.
class ItemList(generics.ListAPIView):
    queryset= Item.objects.order_by('created_at')
    serializer_class = ItemSerializer