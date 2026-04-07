from .models import Document, TypeDocument
from .serializers import DocumentSerializer, TypeDocumentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class DocumentListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def get_queryset(self):
        # Chaque user voit seulement ses propres documents
        return Document.objects.filter(id=self.request.user)

class TypeDocumentListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TypeDocument.objects.all()
    serializer_class = TypeDocumentSerializer

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
class TypeDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TypeDocument.objects.all()
    serializer_class = TypeDocumentSerializer
