from django.urls import path
from .views import BlogPageView, CategoryPageView, BlogPageCreate, BlogPageUpdate

urlpatterns = [
    path('', BlogPageView.as_view(), name="blogPage"),
    path('category/<int:pk>/', CategoryPageView.as_view(), name="categoryPage"),
    path('crear', BlogPageCreate.as_view(), name="blogCreate"),
    path('editar/<int:pk>/', BlogPageUpdate.as_view(), name="blogUpdate"),
]