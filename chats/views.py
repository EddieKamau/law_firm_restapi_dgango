from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView

from chats.models import Chats, Messages
from .serializers import (
    ChatsListSerializers,
    ChatListViewSerializer,
    ChatMessagesSerializer,
    MessagesCreateSerializers
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ChatsListView(ListAPIView):
    queryset = Chats.objects.all()
    serializer_class = ChatsListSerializers
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated,]


class ChatsOwnedListView(ListAPIView):
    # queryset = Chats.objects.filter(users__in=[])
    serializer_class = ChatsListSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Chats.objects.filter(users__in=[self.request.user])



###############################################################################################################


class ChatListApiView(ListAPIView):
    serializer_class = ChatListViewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]
    def get_queryset(self, *args, **kwargs):
        queryset_list = Chats.objects.filter(users__in=[self.request.user])
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(users__username__icontains=query) |
                Q(messages__content__icontains=query)
            ).distinct()
        return queryset_list

    def get_serializer_context(self):
        context = super(ChatListApiView, self).get_serializer_context()
        context.update({
            "user": self.request.user
            # extra data
        })
        return context


class ChatsOwnedDetail(RetrieveUpdateAPIView):
    serializer_class = ChatMessagesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self, *args, **kwargs):

        return Chats.objects.all()

    def get_serializer_context(self):
        context = super(ChatsOwnedDetail, self).get_serializer_context()
        context.update({
            "user": self.request.user
            # extra data
        })
        return context

#
#
# class MessageListAPIView(ListAPIView):
#     queryset = Messages.objects.all()
#     serializer_class = MessagesSerializers
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated,]
#
#
class MessageCreateAPIView(CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesCreateSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

#
# '''
#     def perform_create(self, serializer):
#         serializer.save(user_id=self.request.user)
# '''
#
#
# class MessageDetailView(RetrieveAPIView):
#     queryset = Messages.objects.all()
#     serializer_class = MessagesDetailSerializers
#
#
# # class MessageUpdateView(RetrieveUpdateAPIView):
# #     queryset = Messages.objects.all()
# #     serializer_class = MessagesSerializers
# #
#
# # class MessageDestroyView(DestroyAPIView):
# #     queryset = Messages.objects.all()
# #     serializer_class = MessagesSerializers
