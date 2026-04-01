from django.contrib import admin
from .models import Paiement

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    # Permet de remplir le cas d'utilisation "Consulter payement" [2]
    list_display = ('id_paiement', 'date_paiement', 'montant_total', 'statut', 'brevet', 'utilisateur' , 'document')
    list_filter = ('statut', 'date_paiement')
    search_fields = ('id_paiement', 'brevet__titre')
