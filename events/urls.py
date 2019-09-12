from django.urls import path
from events.views import EventsListApi, EventsCreateApi



urlpatterns = [
    path('', EventsListApi.as_view()),
    path('create/', EventsCreateApi.as_view()),
    ]