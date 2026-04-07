from .models import Notifications
from .serializers import NotificationsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class NotificationsListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
         
class NotificationsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
