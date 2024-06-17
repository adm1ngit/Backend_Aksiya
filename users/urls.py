from django.urls import path
from .views import UserRegistrationView, LoginView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
