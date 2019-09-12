from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User
from cases.models import Cases, Client, CaseEvents


class CasesSerializer(ModelSerializer):
    client = SerializerMethodField()
    class Meta:
        model = Cases
        fields = [
            'id',
            'client',
            'case_name',
            'case_details',
            'case_no',
            'case_status',
            'case_type',
        ]

    def get_client(self, obj):
        client = Client.objects.filter(cases=obj).first()
        user = User.objects.filter(client=client).first()
        return user.username


class CaseDetailSerializer(ModelSerializer):
    client = SerializerMethodField()
    events = SerializerMethodField()
    class Meta:
        model = Cases
        fields = [
            'id',
            'client',
            'case_name',
            'case_details',
            'case_no',
            'case_status',
            'case_type',
            'events',
        ]

    def get_client(self, obj):
        client = Client.objects.filter(cases=obj).first()
        user = User.objects.filter(client=client).first()
        return user.username

    def get_events(self, obj):
        return CaseEventsListSerializer(CaseEvents.objects.filter(case=obj), many=True).data


class CasesCreateSerializer(ModelSerializer):
    class Meta:
        model = Cases
        fields = [
            'client',
            'case_name',
            'case_details',
            'case_no',
            'case_status',
            'case_type',
        ]

class CaseEventsListSerializer(ModelSerializer):
    class Meta:
        model = CaseEvents
        fields = [
            # 'case',
            'event',
            'date',
        ]


class CaseEventsCreateSerializer(ModelSerializer):
    class Meta:
        model = CaseEvents
        fields = [
            'case',
            'event',
            'date',
        ]

