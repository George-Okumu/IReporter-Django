from rest_framework import serializers
from .models import  CustomUser, Admin
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=2,write_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'token','userType',)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=('email','token',)
     
class AdmiRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=2,write_only=True)
    class Meta:
        model = Admin
        fields = ('email', 'username', 'password', 'token','userType',)
        def create(self, validated_data):
            return Admin.objects.create_admin(**validated_data)
     
class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields=('email','token',)

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=('email','password','token',)  
 
               