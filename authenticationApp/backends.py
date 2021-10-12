
from django.conf import settings
from rest_framework import exceptions, authentication
import jwt
from .models import CustomUser
class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = authentication.get_authorization_header(request)
        if not auth_header:
            return None
        token = auth_header.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = CustomUser.objects.get(email = payload['email'])
            return(user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed("Unable to authenticate")
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("Token Expired")
        return super().authenticate(request)
       

        