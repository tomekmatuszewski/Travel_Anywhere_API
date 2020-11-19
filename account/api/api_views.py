from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from account.api.serializers import RegistrationSerializer, UserSerializer, LoginSerializer, ChangePasswordSerializer
from account.api.validation import validate_email, validate_username, error_message, \
    email_lowercase, check_matching_passwords


class RegisterUser(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = validate_username(request.data.get('username'))
        email = validate_email(request.data.get('email'))
        if username or email:
            return Response(error_message(email=email, username=username))
        serializer = self.get_serializer(data=email_lowercase(request.data))
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "User Created Successfully"
            data["username"] = user.username
            data["email"] = user.email
            data["token"] = Token.objects.get(user=user).key

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "destroy", "update", "head"]


class UserProfileView(GenericAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            return self.request.user
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        user = self.get_queryset()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = self.get_queryset()
        serializer = self.get_serializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account updated successfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_queryset()
        user.delete()
        data = {'response': 'User deleted succesfully'}
        return Response(data=data)


class ObtainTokenView(GenericAPIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        context = dict()
        username, password = request.data['username'], request.data['password']
        user = authenticate(username=username, password=password)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            context['response'] = "Successfully authenticated"
            context['id'] = user.id
            context['username'] = username
            context['email'] = user.email
            context['token'] = token.key
            return Response(data=context)
        return Response(data={
            'response': 'Error',
            'message': 'Invalid credentials',
        },
            status=status.HTTP_401_UNAUTHORIZED
        )


class ChangePasswordView(UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "Wrong current password"}, status=status.HTTP_400_BAD_REQUEST)
            elif check_matching_passwords(serializer.data) is None:
                return Response({"new_password": "New password must match"})
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({
                "response": "Successfully changed password"
            },
            status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






















