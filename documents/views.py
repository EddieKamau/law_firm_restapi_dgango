from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView

from documents.serializers import DocumentsListSerializers, DocumentsCreateSerializers
from .models import Documents
from django.db.models import Q

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class DocumentsListApiView(ListAPIView):
    # queryset = Documents.objects.all()
    serializer_class = DocumentsListSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self, *args, **kwargs):
        return Documents.objects.filter(Q(sender=self.request.user) | Q(recipient = self.request.user))


class DocumentsCreateApiView(CreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsCreateSerializers
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated,]


    # def perform_create(self, serializer):
        # serializer.save(sender=self.request.user)










