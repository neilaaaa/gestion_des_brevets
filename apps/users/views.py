from .models import Utilisateur, Role
from .serializers import RoleSerializer, UtilisateurSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UtilisateurListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser] # Seul l'admin peut voir tous les utilisateurs et en créer de nouveaux
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    def get_queryset(self):
        # Chaque user voit seulement ses propres documents
        return Utilisateur.objects.filter(id_user=self.request.user)

class RoleListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser] # Seul l'admin gère les rôles
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UtilisateurDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated] # Un user doit être authentifié pour voir/modifier son profil
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    
    def get_object(self):
        # Un user peut seulement voir/modifier son propre profil
        # sauf si c'est un admin
        if self.request.user.is_staff:
            return super().get_object()
        return self.request.user

class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser] # Seul l'admin gère les rôles
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


