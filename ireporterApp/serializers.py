from rest_framework import serializers
from .models import RedFlag,Intervention
class RedFlagSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = RedFlag
        fields = ('redFlag_image', 'title', 'description', 'redFlag_video','user', 'status', 'redFlag_location',)
class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields=('subject','description','location',) 