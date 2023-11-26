from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from oauth.serializers import UserSerializer
from oauth.tasks import send_email_message_task


class RegisterUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_email_message_task.delay(serializer.data["username"], serializer.data["email"])
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {'data': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
