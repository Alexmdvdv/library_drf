from django.urls import path

from library.views import BaseBookAPIView, BookAPIView, UserInfoRegistrationView, UserApiView

urlpatterns = [
    path('library/<int:pk>/', BaseBookAPIView.as_view()),
    path('library/', BookAPIView.as_view()),
    path('reader/', UserInfoRegistrationView.as_view()),
    path('reader/<int:pk>/', UserApiView.as_view())
]
