
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render
from rest_framework import generics, permissions, status, views, exceptions
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegistrationSerializer, LoginSerializer
from django.urls import reverse
from .EmailHandler import EmailHandlerClass
import jwt
from django.contrib import auth
from django.conf import settings
class RegistrationAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer
    def post(self, request):
        user_request = request.data
        serializer = self.serializer_class(data=user_request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email = user_data['email'])
        token = RefreshToken.for_user(user).access_token
        reverse_link = reverse('verify-email')
        absolute_url = 'http://'+get_current_site(request).domain+reverse_link+'?token='+str(token)
        email_body = "Hello"+" " + user.username  +" "+ "click the link bellow to activate your account \n"+absolute_url
        data ={'email_body':email_body, 'email_to':user.email,'email_subject': 'Activate Ireporter Account'}
        EmailHandlerClass.sendEmail(data)
        return Response(user_data, status=status.HTTP_200_OK)
        
class VerifyEmail(views.APIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            #decode the token from the email
            payload = jwt.decode(token, settings.SECRET_KEY, 'HS256',)
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_email_verified:
                user.is_email_verified = True
                user.save()
            return Response({'message': 'Email Successfully Verified'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Your Token has expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Token Is Invalid'}, status=status.HTTP_400_BAD_REQUEST)
class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = auth.authenticate(username=email, password=password)
        if user:
            serializer = LoginSerializer(user)
            if not user.is_email_verified:
                return Response({'Denied':'Account not active, Verify your email address to activate your account'})
            else:
                data ={
                    'message':'Login Successfull',
                    'token':serializer.data.get('token')
                }
                return Response(data, status=status.HTTP_200_OK)
        return Response({'Error':'User with credentials do not exist'}, status=status.HTTP_401_UNAUTHORIZED)

                
    