from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import CustomUserSerializer
from .models import CustomUser

class UserRegistrationView(generics.CreateAPIView):
    # queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(email="collins@gmail.com", password="12345678") #authenticate(email=request.data['email'], password=request.data['password'])
        if user:
            
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        else:
            return Response({'error': 'Invalid credentials'}, status=401)