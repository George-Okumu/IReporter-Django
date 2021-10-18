from django.http import request
from requests.adapters import Response

from authenticationApp import serializers
from .models import RedFlag
from .serializers import RedFlagSerializer, RedFlagAdminActionsSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsAdmin

class RedFlagList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
  
    # def get_queryset(self):
        
    #     return super().get_queryset()


class RedFlagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer
    def get_queryset(self):
        return super().get_queryset(user = self.request.user)
    def perform_update(self, serializer):
        return super().perform_update(serializer)

class RedFlagAdminActions(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdmin]
    queryset = RedFlag.objects.all()
    lookup_field='pk'
    serializer_class = RedFlagAdminActionsSerializer

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        return super().retrieve(request, *args, **kwargs)
    def perform_update(self, serializer):
        user =self.get_object()
        print(user)
        return super().perform_update(serializer)
  
   

