from rest_framework import serializers
from .models import UserText

class UserTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserText
        fields = ["id", "text"]