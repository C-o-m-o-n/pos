from django.shortcuts import render
from django.rest_framework import generics, permissions
from django.rest_framework.response import Response
from django.rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class UserRegistrationView(generics.CreteApiView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        data = {}
        if serializer.is_valid():
            custom_user = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = custom_user.email
            data['username'] = custom_user.username
            token = Token.objects.get(user=custom_user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

class UserLoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        username = data.get("username", "")
        password = data.get("password", "")
        custom_user = authenticate(username=username, password=password)
        if custom_user:
            login(request, custom_user)
            serializer = CustomUserSerializer(custom_user)
            return Response(serializer.data)
        return Response("Invalid Credentials")
    