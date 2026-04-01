from django.db import models
from django.conf import settings

class Recours(models.Model):
    # Les statuts correspondent exactement à l'énumération du diagramme de classe
    STATUT_CHOICES = [
        ('EN_COURS', 'En cours'),
        ('TRAITE', 'Traité'),
        ('REFUSE', 'Refusé'),
    ]

    id_recours = models.AutoField(primary_key=True) # id_recours: int [2]
    date_depot = models.DateField() # date_depot: date [2]
    motif = models.CharField(max_length=255) # motif: string [2]
    description = models.TextField() # description: string [2]
    statut = models.CharField(
        max_length=20, 
        choices=STATUT_CHOICES, 
        default='EN_COURS'
    ) # statut: enum [2]
    date_traitement = models.DateField(null=True, blank=True) # date_traitement: date [2]

    # Relations basées sur le schéma relationnel [2]
    # Un utilisateur (1,1) fait (0,*) recours
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='recours_faits'
    )
    # Un brevet (1,1) est concerné par (0,*) recours
    brevet = models.ForeignKey(
        'brevets.Brevet', 
        on_delete=models.CASCADE,
        related_name='recours_associes'
    )

    class Meta:
        verbose_name = "Recours"
        verbose_name_plural = "Recours"

    def __str__(self):
        return f"Recours {self.id_recours} - {self.motif}"
