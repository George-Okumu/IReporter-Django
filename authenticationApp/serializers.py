from rest_framework import serializers
from .models import  CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=2,write_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'token',)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

     
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'is_admin',)
        read_only_fields = ('modified',)

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=('email','token',)  