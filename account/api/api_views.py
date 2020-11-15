from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from account.api.serializers import RegistrationSerializer


class RegisterUser(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data[
                "response"
            ] = "User Created Successfully"
            data["username"] = user.username
            data["email"] = user.email
            data["token"] = Token.objects.get(user=user).key

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
