from django.db import models
from django.conf import settings

class Notification(models.Model):
    # Attributs conformes au diagramme de classe [1]
    id_notif = models.CharField(max_length=50, primary_key=True) # id_notif:string
    date_notif = models.DateTimeField(auto_now_add=True) # date_notif:DateTime
    message = models.TextField() # message:string
    etat = models.BooleanField(default=False) # etat:boolean (False = non lu, True = lu)

    # Relation (1,1) Utilisateur <-> (0,*) Notifications [1]
    # Chaque notification appartient à un utilisateur spécifique (id_user*)
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-date_notif'] # Les plus récentes en premier

    def __str__(self):
        return f"Notif pour {self.utilisateur.username} - {self.date_notif.strftime('%d/%m/%Y')}"
