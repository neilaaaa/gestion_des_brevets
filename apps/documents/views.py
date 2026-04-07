from django.views.generic import ListView, DetailView
from .models import Document, TypeDocument
from .serializers import DocumentSerializer, TypeDocumentSerializer
from rest_framework import generics

class DocumentListView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class TypeDocumentListView(generics.ListCreateAPIView):
    queryset = TypeDocument.objects.all()
    serializer_class = TypeDocumentSerializer

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
class TypeDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeDocument.objects.all()
    serializer_class = TypeDocumentSerializer
