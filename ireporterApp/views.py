from django.http import request
from requests.adapters import Response

from authenticationApp.EmailHandler import EmailHandlerClass
from .models import RedFlag
from .serializers import RedFlagSerializer, RedFlagAdminActionsSerializer
from .models import Intervention
from .serializers import InterventionSerializer, RedFlagSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsAdmin


class RedFlagList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RedFlagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class RedFlagAdminActions(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdmin]
    queryset = RedFlag.objects.all()
    lookup_field='pk'
    serializer_class = RedFlagAdminActionsSerializer

    def perform_update(self, serializer):
        user_type = self.request.user.is_admin
        print(user_type)
        return super().perform_update(serializer)

class InterventionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Intervention.objects.all()
    serializer_class = InterventionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class InterventionList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
