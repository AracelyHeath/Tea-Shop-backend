from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'

class CartAddSerializer(serializer.ModelSerializer):
    class Meta:
        model=Cart
        fields:'__all__'
