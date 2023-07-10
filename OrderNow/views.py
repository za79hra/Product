from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status

class Register(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User created successfully." , "data": serializer.data}, status=status.HTTP_200_OK)
            # return Response(serializer.data, status=status.HTTP_200_OK)
        if 'username' in serializer.errors:
            errors = serializer.errors['username']
            if 'unique' in errors:
                return Response({"message": "this username has already been used."}, status=status.HTTP_403_FORBIDDEN)

        return Response({"message": "User creation failed.", "errors": serializer.errors}, status=400)
        # return Response(serializer.errors, status=400)

