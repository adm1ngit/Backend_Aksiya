from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from .models import User

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        password = request.data.get("password")

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return Response({'error': "Error 404 User Not Found "}, status=404)

        if not user.check_password(password):
            return Response({'error': 'Invalid phone number or password'}, status=401)

        # Session-based authentication (consider CSRF protection)
        request.session["user_id"] = user.id  # Store user ID in session
        return Response({"message": "Login successful"})