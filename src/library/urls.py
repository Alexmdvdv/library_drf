from django.urls import path

from library.views import BaseBookAPIView, BookAPIView

urlpatterns = [
    path('library/<int:pk>/', BaseBookAPIView.as_view()),
    path('library/', BookAPIView.as_view())
]
