from django.urls import path
from .views import HistoryPageView

urlpatterns = [
    path('', HistoryPageView.as_view(), name="historyPage"),
]