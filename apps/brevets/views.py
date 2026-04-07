from .models import DemandeBrevet, Deposant, Inventeur, Brevet
from .serializers import DemandeBrevetSerializer, DeposantSerializer, InventeurSerializer, BrevetSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class DemandeBrevetListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DemandeBrevet.objects.all()
    serializer_class = DemandeBrevetSerializer
    
class DemandeBrevetDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DemandeBrevet.objects.all()
    serializer_class = DemandeBrevetSerializer  
    
class DeposantListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Deposant.objects.all()
    serializer_class = DeposantSerializer
    
class DeposantDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Deposant.objects.all()
    serializer_class = DeposantSerializer
    
class InventeurListView(generics.ListCreateAPIView):  
    permission_classes = [IsAuthenticated]
    queryset = Inventeur.objects.all()
    serializer_class = InventeurSerializer
    
class InventeurDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Inventeur.objects.all()
    serializer_class = InventeurSerializer
    
class BrevetListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Brevet.objects.all()
    serializer_class = BrevetSerializer 
    
class BrevetDetailView(generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = [IsAuthenticated]
    queryset = Brevet.objects.all()
    serializer_class = BrevetSerializer
