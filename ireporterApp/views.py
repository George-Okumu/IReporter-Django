from .models import RedFlag
from .serializers import RedFlagSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class RedFlagList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer
    #perfom user redflag creation
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user.pk)


class RedFlagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer