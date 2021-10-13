from django.http import request
from .models import RedFlag
from .serializers import RedFlagSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class RedFlagList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # def get_queryset(self):
        
    #     return super().get_queryset()


class RedFlagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer
    def perform_update(self, serializer):
        user_type = self.request.user.is_admin
        print(user_type)
        return super().perform_update(serializer)