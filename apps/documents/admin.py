from django.contrib import admin
# On importe les modèles depuis le fichier models.py
from .models import Typedocument, Documents 

@admin.register(Typedocument)
class TypedocumentAdmin(admin.ModelAdmin):
    # Attributs définis dans le Diagramme de classe général [1]
    list_display = ('id_type', 'nom_type', 'taille_max', 'format_autorise')
    search_fields = ('nom_type',)

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    # Pour le Use Case "Consulter document" de l'Agent [3]
    list_display = ('id_document', 'nom_document', 'typedocument', 'date_ajout', 'utilisateur', 'brevet')
    list_filter = ('typedocument', 'date_ajout')
    search_fields = ('nom_document',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Traçabilité de l'utilisateur qui effectue l'action "Ajouter" [3]
            obj.utilisateur = request.user
        super().save_model(request, obj, form, change)
