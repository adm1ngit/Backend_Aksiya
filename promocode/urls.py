from django.urls import path
from .views import UserTextCreateView, UserTextListView

urlpatterns = [
    path('texts/', UserTextListView.as_view(), name='text-list'),
    path('texts/create/', UserTextCreateView.as_view(), name='text-create'),
]
