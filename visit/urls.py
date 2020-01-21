from django.urls import path
from .views import VisitPageView

urlpatterns = [
    path('', VisitPageView.as_view(), name="visitPage"),
]