from .models import Paiement
from .serializers import PaiementSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class PaiementListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer
    
class PaiementDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer
