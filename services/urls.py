from django.urls import path
from .views import ServicesPageView

urlpatterns = [
    path('', ServicesPageView.as_view(), name="servicesPage"),
]