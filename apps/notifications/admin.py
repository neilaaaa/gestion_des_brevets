from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    # Permet de consulter l'historique des alertes système
    list_display = ('id_notif', 'utilisateur', 'message', 'date_notif', 'etat')
    list_filter = ('etat', 'date_notif')
    search_fields = ('message', 'utilisateur__username', 'id_notif')
    
    # On peut marquer manuellement comme lu/non lu dans l'admin
    list_editable = ('etat',)
