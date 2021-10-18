
from os import path
from django.conf import settings
from rest_framework import exceptions, authentication
import jwt
from .models import  CustomUser
class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = authentication.get_authorization_header(request)
        
        if not auth_header:
            return None
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")
        if len(auth_token)!=2:
            raise exceptions.AuthenticationFailed('Token format is incorrect')
        token = auth_token[1]
              
        try:
            payload=jwt.decode(token, key=settings.SECRET_KEY, algorithms="HS256")
            email = payload['email']
            user = CustomUser.objects.get(email= email)
            return(user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed("Unable to authenticate, token is invalid")
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("Token Expired, login again")
        except CustomUser.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed("User does not exist")
        return super().authenticate(request)
       

        