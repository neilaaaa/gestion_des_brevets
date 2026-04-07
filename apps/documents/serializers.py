from rest_framework import serializers
from .models import TypeDocument, Document

class TypeDocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = TypeDocument
    fields = '__all__'
    
class DocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Document
    fields = '__all__'