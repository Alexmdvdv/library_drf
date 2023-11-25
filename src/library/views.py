from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from library.models import Book, UserInfo
from library.serializers import BookSerializer, UserInfoSerializer
from library.tasks import send_email_message_task


class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BaseBookAPIView(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)

        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def patch(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterUserAPIView(APIView):
    """
    К комментарию в models.py, в заданий говорилось о регистарации без авторизации пользователя,
    решил сделать так, возможно имелось ввиду "добавление" пользователя
    """

    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_email_message_task.delay(serializer.data["username"], serializer.data["email"])

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):

    def get(self, request, pk):
        user = UserInfo.objects.get(pk=pk)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)
