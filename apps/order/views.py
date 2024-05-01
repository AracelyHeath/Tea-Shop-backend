from django.shortcuts import render
from .models import Order, OrderItem
from .serializers import OrderSerializer
from apps.user.mixins import CustomLoginRequiredMixin
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from apps.cart.models import Cart
from .forms import OrderForm, OrderItemForm


# Create your views here.
class OrderAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset=Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        self.queryset=cart.objects.order_by('-created_at').filter(user=request.login_user)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data['user']=request.login_user.id
        order_form=OrderForm(request.data)
        if not order_form.is_valid():
            response=Response({'error':'Request data not correct'},status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer= JSONRenderer()
            response.accepted_media_type= 'application/json'
            response.renderer_context={}
            return response

        order=order_form.save()
        carts=Cart.objects.filter(user=request.login_user)    
        for cart in carts:
            order_item_form=OrderItemForm({'order':order.id, 'item':cart.item.id, 'quantity':cart.quantity})
            order_item_form.save()

        carts.delete()
        serializer=OrderSerializer([order], many=True)
        return Response(serializer.data[0])    