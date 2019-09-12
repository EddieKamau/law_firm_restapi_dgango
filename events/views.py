from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView

from events.serializers import EventsCreateSerializer, EventsListSerializer
from .models import Events
from django.db.models import Q

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class EventsListApi(ListAPIView):
    serializer_class = EventsCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Events.objects.filter(owner=self.request.user)


class EventsCreateApi(CreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

