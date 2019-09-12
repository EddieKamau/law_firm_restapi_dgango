from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from cases.models import Cases, Lawyer, Client, CaseEvents
from cases.serializers import CasesSerializer, CasesCreateSerializer, CaseEventsListSerializer, CaseDetailSerializer, \
    CaseEventsCreateSerializer
from django.contrib.auth.models import User

from .permissions import IsLawyer

from django.db.models import Q



from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class CasesListView(ListAPIView):

    serializer_class = CasesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cases.objects.filter(Q(lawyer=Lawyer.objects.filter(lawyer_id=self.request.user).first()) | Q(client=Client.objects.filter(client_id=self.request.user).first()))
        return queryset


class CasesCreateView(CreateAPIView):
    queryset = Cases.objects.all()
    serializer_class = CasesCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLawyer,]

    def perform_create(self, serializer):
        lawyer = Lawyer.objects.filter(lawyer_id=self.request.user).first()
        serializer.save(lawyer = lawyer)

class CasesDetailView(RetrieveUpdateAPIView):
    serializer_class = CaseDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cases.objects.filter(Q(lawyer=Lawyer.objects.filter(lawyer_id=self.request.user).first()) | Q(client=Client.objects.filter(client_id=self.request.user).first()))
        return queryset

#
# class CaseEventsListView(ListAPIView):
#     queryset = CaseEvents.objects.all()
#     serializer_class = CaseEventsListSerializer


class CaseEventsCreateView(CreateAPIView):
    queryset = CaseEvents.objects.all()
    serializer_class = CaseEventsCreateSerializer

