from django.urls import path

from library.views import BaseBookAPIView, BookAPIView, BaseUserAPIView, UserAPIView

urlpatterns = [
    path('library/<int:pk>/', BaseBookAPIView.as_view()),
    path('library/', BookAPIView.as_view()),
    path('reader/<int:pk>/', BaseUserAPIView.as_view()),
    path('reader/', UserAPIView.as_view()),
]
