from .models import User
from rest_framework import status
from rest_framework.response import Response
import datetime
from rest_framework.renderers import JSONRenderer

class CustomLoginRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            response= Response({'error':'please set auth token'},status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer= JSONRenderer()
            response.accepted_media_type= 'application/json'
            response.renderer_context={}
            return response
        
        token= request.headers['Authorization']
        now= datetime.datetime.now()
        login_user= User.objects.filter(token=token, token_expires__gt=now)

        if len(login_user) == 0:
            response= Response({'error':'token is expired or invalid'},status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer= JSONRenderer()
            response.accepted_media_type= 'application/json'
            response.renderer_context={}
            return response

        request.login_user= login_user[0]
        return super().dispatch(request, *args, **kwargs)

