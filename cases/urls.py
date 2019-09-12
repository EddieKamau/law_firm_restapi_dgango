from django.urls import path, include
from cases.views import CasesCreateView, CasesListView, CasesDetailView, CaseEventsCreateView

urlpatterns = [
    path('', CasesListView.as_view()),
    path('<int:pk>/', CasesDetailView.as_view()),
    path('create/', CasesCreateView.as_view()),
    # path('events/', CaseEventsListView.as_view()),
    path('events/create/', CaseEventsCreateView.as_view()),

]