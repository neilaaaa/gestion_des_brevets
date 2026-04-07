from django.urls import path
from . import views

urlpatterns = [
  path('Document/', views.DocumentListView.as_view(), name='Document-view'),
  path('Document/<int:pk>/', views.DocumentDetailView.as_view(), name='Document-update'),
  path('TypeDocument/', views.TypeDocumentListView.as_view(), name='TypeDocument-view'),
  path('TypeDocument/<int:pk>/', views.TypeDocumentDetailView.as_view(), name='TypeDocument-update')
]