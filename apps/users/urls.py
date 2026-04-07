from django.urls import path
from. import views

urlpatterns = [
  path('User/', views.UtilisateurListView.as_view(), name='Utilisateur-view'),
  path('User/<str:pk>/', views.UtilisateurDetailView.as_view(), name='Utilisateur-update'),
  path('Role/', views.RoleListView.as_view(), name='Role-view'),
  path('Role/<int:pk>/', views.RoleDetailView.as_view(), name='Role-update'),
]