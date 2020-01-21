from django.urls import path
from .views import LegalPageView

urlpatterns = [
    path('<int:pk>/<slug:slug>', LegalPageView.as_view(), name="legalPage"),
]