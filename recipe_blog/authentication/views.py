from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    UserRegistrationSerializer,
)


class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'You are successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)