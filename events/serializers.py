from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Events



class EventsListSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = [
            'title',
            'location',
            'notes',
            'start_date',
            'end_date',
        ]



class EventsCreateSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = [
            'title',
            'location',
            'notes',
            'start_date',
            'end_date',
        ]


