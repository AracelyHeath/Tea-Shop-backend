from django.shortcuts import render
from .serializers import CartSerializer, CartAddSerializer
from apps.user.mixins import CustomLoginRequiredMixin
from .models import Cart
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# Create your views here.
class CartList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset=cart.ojects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        self.queryset=cart.objects.order_by('-created_at').filter(user=request.login_user)
        return self.list(request, *args, **kwargs) 


class CartAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset=cart.ojects.all()
    serializer_class = CartAddSerializer

    def post(self, request, *args, **kwargs):
        # set the user who login 
        request.data['user']= request.login_user.id
        return self.create(request, *args. **kwargs)

class CartDelete(CustomLoginRequiredMixin, generics.DestroyAPIView):
    queryset=cart.ojects.all()
    serializer_class = CartAddSerializer

    def delete(self, request, *args, **kwargs):
        cart=cart.objects.get(pk=self.kwargs['pk'])
        if cart.user.id != request.login_user.id:
            response=Response({'Error': 'You cannot delete cart list not owned by you. Be Careful'}, status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer=JSONRenderer()
            response.accepted_media_type='application/json'
            response.renderer_context={}
            return response

        return self.destroy(request, *args, **kwargs)    

