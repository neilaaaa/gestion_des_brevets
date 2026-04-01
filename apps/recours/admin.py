from django.contrib import admin
from .models import Recours

@admin.register(Recours)
class RecoursAdmin(admin.ModelAdmin):
    # Permet de remplir le cas d'utilisation "Consulter recours" [3]
    list_display = ('id_recours', 'motif', 'statut', 'date_depot', 'brevet', 'utilisateur')
    
    # Filtres pour aider l'Agent à gérer les dossiers prioritaires
    list_filter = ('statut', 'date_depot')
    
    # Recherche par motif ou par titre du brevet concerné
    search_fields = ('motif', 'brevet__titre', 'id_recours')
    
    # Organisation du formulaire pour l'action "Modifier/Ajouter recours" [3]
    fieldsets = (
        ('Informations sur le Recours', {
            'fields': ('motif', 'description', 'statut')
        }),
        ('Dates Clés', {
            'fields': ('date_depot', 'date_traitement')
        }),
        ('Rattachements', {
            'fields': ('utilisateur', 'brevet')
        }),
    )
