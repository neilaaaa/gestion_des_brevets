from django.contrib import admin
from .models import Deposant, Inventeur, DemandeBrevet, Brevet

class DeposantInline(admin.StackedInline):
    model = Deposant
    extra = 0 # 0 au lieu de 1 car c'est un OneToOneField et un minimum pour plus de clarté
    can_delete = False # Le déposant est obligatoire

class InventeurInline(admin.TabularInline):
    model = Inventeur
    extra = 1

@admin.register(Deposant)
class DeposantAdmin(admin.ModelAdmin):
    list_display = ('id_dep', 'nom_dep', 'prenom_dep', 'denomination', 'nationalite', 'id_demande')
    search_fields = ('nom_dep', 'denomination', 'id_dep')
    list_filter = ('nationalite',)

@admin.register(Inventeur)
class InventeurAdmin(admin.ModelAdmin):
    list_display = ('id_inv', 'nom_inv', 'prenom_inv', 'id_demande')
    search_fields = ('nom_inv', 'prenom_inv', 'id_inv')
    # Permet de filtrer les inventeurs par le titre de la demande
    list_filter = ('id_demande__titre',)

@admin.register(DemandeBrevet)
class DemandeBrevetAdmin(admin.ModelAdmin):
    list_display = ('id_demande', 'titre', 'statut', 'num_depo', 'date_depo', 'id_user')
    list_filter = ('statut', 'date_depo', 'pays_origine')
    search_fields = ('titre', 'id_demande', 'num_depo')
    inlines = [DeposantInline, InventeurInline]
    
    fieldsets = (
        ('Identification', {
            'fields': ('id_demande', 'titre', 'nature', 'statut')
        }),
        ('Détails du Dépôt', {
            'fields': ('num_depo', 'date_depo', 'pays_origine', 'numdemande_CA', 'date_CA')
        }),
        ('Réception et Mandat', {
            'fields': ('mandataire', 'date_pouvoir', 'prepose_reception', 'lieu_reception', 'date_reception')
        }),
        ('Rattachement Utilisateur', {
            'fields': ('id_user', 'autre_info')
        }),
    )

@admin.register(Brevet)
class BrevetAdmin(admin.ModelAdmin):
    list_display = ('id_brevet', 'num_brevet', 'titre', 'statut', 'date_sortie', 'titulaire', 'id_demande')
    list_filter = ('statut', 'date_sortie')
    search_fields = ('titre', 'id_brevet', 'titulaire')
    