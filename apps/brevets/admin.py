from django.contrib import admin
from .models import Deposant, Inventeur, DemandeBrevet, Brevet

# --- Configuration pour les Déposants ---
@admin.register(Deposant)
class DeposantAdmin(admin.ModelAdmin):
    list_display = ('id_dep', 'nom_dep', 'prenom_dep', 'denomination', 'nationalite')
    search_fields = ('nom_dep', 'denomination', 'id_dep')
    list_filter = ('nationalite',)

# --- Configuration pour les Inventeurs ---
@admin.register(Inventeur)
class InventeurAdmin(admin.ModelAdmin):
    list_display = ('id_inv', 'nom_inv', 'prenom_inv', 'demande')
    search_fields = ('nom_inv', 'prenom_inv', 'id_inv')
    # Permet de filtrer les inventeurs par le titre de la demande associée
    list_filter = ('demande__titre',)

# --- Configuration pour les Demandes de Brevet (Action centrale de l'Agent/Responsable) ---
@admin.register(DemandeBrevet)
class DemandeBrevetAdmin(admin.ModelAdmin):
    # list_display permet de "Consulter" rapidement les infos clés [2]
    list_display = ('id_demande', 'titre', 'statut', 'num_depot', 'date_depot', 'user')
    
    # list_filter aide le Responsable à trouver les demandes à "Vérifier" [1]
    list_filter = ('statut', 'date_depot', 'pays_origine')
    
    # search_fields facilite la recherche par titre ou identifiant
    search_fields = ('titre', 'id_demande', 'num_depot')
    
    # Organisation des champs par sections dans le formulaire de modification
    fieldsets = (
        ('Identification', {
            'fields': ('id_demande', 'titre', 'nature', 'statut')
        }),
        ('Détails du Dépôt', {
            'fields': ('num_depot', 'date_depot', 'pays_origine', 'numdemande_CA', 'date_CA')
        }),
        ('Réception et Mandat', {
            'fields': ('mandataire', 'date_pouvoir', 'prepose_reception', 'lieu_reception', 'date_reception')
        }),
        ('Rattachement', {
            'fields': ('user', 'deposant', 'autre_info')
        }),
    )

# --- Configuration pour les Brevets validés ---
@admin.register(Brevet)
class BrevetAdmin(admin.ModelAdmin):
    list_display = ('id_brevet', 'num_brevet', 'titre', 'status', 'date_sortie', 'titulaire')
    
    # Les statuts correspondent exactement à l'énumération du diagramme de classe [3]
    list_filter = ('status', 'date_sortie')
    search_fields = ('titre', 'id_brevet', 'titulaire')
    
    # Permet de lier facilement le brevet à sa demande d'origine
    autocomplete_fields = ['demande']