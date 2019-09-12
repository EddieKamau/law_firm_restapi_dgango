from django.urls import path, include
from rest_framework.authtoken import views


from firm.views import (
    ClientCreate,
    ClientDelete,
    ClientListView,
    SignUpApi,
    ClientForgottenPassword,
    ResetPassword
)


urlpatterns = [
    # path('messages/', MessageListAPIView.as_view()),
    # path('messages/<int:pk>/', MessageDetailView.as_view()),
    # # path('messages/<int:pk>/update/', MessageUpdateView.as_view()),
    # # path('messages/<int:pk>/delete/', MessageDestroyView.as_view()),
    path('login/', views.obtain_auth_token),
    path('clients/', ClientListView.as_view()),
    path('client/create/', ClientCreate.as_view()),
    path('client/forgotten_password/', ClientForgottenPassword.as_view()),
    path('client/reset_password/', ResetPassword.as_view()),
    path('client/signup', SignUpApi.as_view()),
    path('client/<int:pk>/delete/', ClientDelete.as_view()),

    # chats
    path('chats/', include('chats.urls')),

    # documents
    path('documents/', include('documents.urls')),


    # cases
    path('cases/', include('cases.urls')),

    # events
    path('events/', include('events.urls')),


]