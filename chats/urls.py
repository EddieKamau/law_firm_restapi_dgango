from django.urls import path
from chats.views import ChatsListView, ChatsOwnedListView, ChatListApiView, ChatsOwnedDetail, MessageCreateAPIView



urlpatterns = [
    path('', ChatsListView.as_view()),
    path('<int:pk>', ChatsOwnedListView.as_view()),
    path('view/', ChatListApiView.as_view()),
    path('view/<int:pk>/', ChatsOwnedDetail.as_view()),

    path('messages/create/', MessageCreateAPIView.as_view()),

]