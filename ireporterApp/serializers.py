from django.db import models
from rest_framework import serializers
from .models import RedFlag
class RedFlagSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = RedFlag
        fields = ('redFlag_image', 'title', 'description', 'redFlag_video','user', 'status', 'redFlag_location',)
     
class RedFlagAdminActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedFlag
        fields = ('id','redFlag_image', 'title', 'description', 'redFlag_video','user', 'status', 'redFlag_location',)
        read_only_fields = ('id','redFlag_image', 'title', 'description', 'redFlag_video','user', 'redFlag_location',)

        def update(self, instance, validated_data):
            status = validated_data.get('status', self.status)
            print(status)
            
