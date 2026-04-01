from django.db import models
from django.conf import settings

class Paiement(models.Model):
    STATUT_CHOICES = [
        ('payer', 'Payer'),
        ('non_payer', 'Non Payer'),
    ]

    id_paiement = models.AutoField(primary_key=True)
    date_paiement = models.DateField()
    montant_total = models.FloatField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)

    # Relations basées sur le schéma relationnel [1]
    brevet = models.ForeignKey('brevets.Brevet', on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    document = models.ForeignKey(
    'documents.Documents', 
    on_delete=models.SET_NULL, 
    null=True, 
    blank=True,
    related_name='paiements'
)
    class Meta:
        verbose_name = "Paiement"
        verbose_name_plural = "Paiements"

    def __str__(self):
        return f"Paiement {self.id_paiement} - {self.montant_total} DA"
