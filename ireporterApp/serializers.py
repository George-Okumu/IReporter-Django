from django.db import models
from rest_framework import serializers
from .models import RedFlag,Intervention
class RedFlagSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = RedFlag
        fields = ('id','redFlag_image', 'title', 'description', 'redFlag_video','user', 'status', 'redFlag_location',)
     
class RedFlagAdminActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedFlag
        fields = ('id','redFlag_image', 'title', 'description', 'redFlag_video','user', 'status', 'redFlag_location',)
        read_only_fields = ('id','redFlag_image', 'title', 'description', 'redFlag_video','user', 'redFlag_location',)  
        fields = ('redFlag_image', 'title', 'description', 'redFlag_video','user', 'status', 'redFlag_location',)
class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields=('subject','description','location','status', 'user','intervention_image',) 
