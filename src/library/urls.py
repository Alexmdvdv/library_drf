from django.urls import path

from library.views import BaseBookAPIView, BookAPIView, RegisterUserAPIView, UserAPIView

urlpatterns = [
    path('library/<int:pk>/', BaseBookAPIView.as_view()),
    path('library/', BookAPIView.as_view()),
    path('reader/<int:pk>/', UserAPIView.as_view()),
    path('reader/', RegisterUserAPIView.as_view()),
]
