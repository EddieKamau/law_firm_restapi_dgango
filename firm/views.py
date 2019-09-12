from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from django.db.models import Q


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from django.contrib.auth.models import User

from firm.models import Lawyer
from chats.models import Messages, Chats
from firm.permissions import isStaff
from .serializers import (
    ClientSerializerView,
    ClientCreateSerializer,
    SignUp,
    ClientForgottenPasswordSerializer,
    ResetPasswordSerializer,
    UsernameSerializer
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class ClientCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ClientCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


class ClientDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ClientSerializerView
    authentication_classes = [TokenAuthentication,]
    permission_classes = [isStaff]


class ClientForgottenPassword(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ClientForgottenPasswordSerializer

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = ClientForgottenPasswordSerializer(data=data)
    #     if serializer.is_valid(raise_exception=True):
    #         new_data = serializer.data
    #         return Response(new_data, status=HTTP_200_OK)
    #
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




class ClientListView(ListAPIView):
    serializer_class = ClientSerializerView
    authentication_classes = [TokenAuthentication,]
    permission_classes = [isStaff]

    def get_queryset(self):
        queryset = User.objects.filter(is_staff=False)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(client__cases__case_no__icontains=query)
            ).distinct()

        return queryset


class ResetPassword(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer
    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = ResetPasswordSerializer(data=data)
    #     if serializer.is_valid(raise_exception=True):
    #         new_data = serializer.data
    #         return Response(new_data, status=HTTP_200_OK)
    #
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class SignUpApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUp



class UserNameApi(ListAPIView):
    serializer_class = UsernameSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
