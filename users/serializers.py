from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')

        return attrs

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user