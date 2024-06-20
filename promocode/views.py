from rest_framework import generics
from .models import UserText
from .serializers import UserTextSerializer

class UserTextCreateView(generics.CreateAPIView):
    queryset = UserText.objects.all()
    serializer_class = UserTextSerializer

class UserTextListView(generics.ListAPIView):
    queryset = UserText.objects.all()
    serializer_class = UserTextSerializer
