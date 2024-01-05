from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = "__all__"
