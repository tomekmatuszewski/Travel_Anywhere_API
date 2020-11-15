from rest_framework import generics, status
from rest_framework.response import Response

from account.api.serializers import RegistrationSerializer


class RegisterUser(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data[
                "response"
            ] = "User Created Successfully.  Now perform Login to get your token"
            data["username"] = user.username
            data["email"] = user.email

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
