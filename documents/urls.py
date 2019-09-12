from django.urls import path
from documents.views import DocumentsListApiView, DocumentsCreateApiView



urlpatterns = [
    path('', DocumentsListApiView.as_view()),
    path('create/', DocumentsCreateApiView.as_view()),
    ]