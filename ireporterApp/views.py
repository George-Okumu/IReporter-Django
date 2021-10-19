from django.http import request
from requests.adapters import Response

from authenticationApp.EmailHandler import EmailHandlerClass
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
        status= serializer.validated_data.get('status')
        print(status)
        user =self.get_object()
        email_body = "Hello"+" " + user  +" "+ "Your redflag status was updated by Admin to \n"+status
        data ={'email_body':email_body, 'email_to':user,'email_subject': 'REDFLAG STATUS UPDATE'}
        EmailHandlerClass.sendEmail(data)
        return super().perform_update(serializer)
  
   

