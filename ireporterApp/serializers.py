from rest_framework import serializers
from .models import RedFlag
class RedFlagSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    status = serializers.ReadOnlyField(source='status.status')
    class Meta:
        model = RedFlag
        fields = ('redFlag_image', 'title', 'description', 'redFlag_video','user', 'status', 'redFlag_location',)
        # def create(self, validated_data):
        #     status_data = validated_data.pop('status')
        #     status = RedFlag.objects.get(description=status_data['description'])  
        #     job = RedFlag.objects.create(status=status,...) #categy object found by it's description
        #     return job
