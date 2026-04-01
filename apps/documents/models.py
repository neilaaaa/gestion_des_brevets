from django.db import models
from django.conf import settings

# --- Type de Document ---
class Typedocument(models.Model):
    # Attributs du diagramme [1]
    id_type = models.AutoField(primary_key=True) # id_type: int
    nom_type = models.CharField(max_length=100)
    description = models.TextField()
    taille_max = models.IntegerField() # en Ko ou Mo
    format_autorise = models.CharField(max_length=50) # ex: .pdf, .docx

    def __str__(self):
        return self.nom_type

# --- Documents ---
class Documents(models.Model):
    # Attributs du diagramme [1]
    id_document = models.AutoField(primary_key=True) # id_document: int
    nom_document = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='brevets/documents/') # fichier: string
    date_ajout = models.DateField(auto_now_add=True) # date_ajout: date

    # Relations basées sur le schéma relationnel [1]
    typedocument = models.ForeignKey(Typedocument, on_delete=models.CASCADE) # id_type*
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # id_user*
    
    # Relations optionnelles vers les dossiers (selon le schéma relationnel)
    brevet = models.ForeignKey('brevets.Brevet', on_delete=models.CASCADE, null=True, blank=True)
    demande = models.ForeignKey('brevets.DemandeBrevet', on_delete=models.CASCADE, null=True, blank=True)
    paiement = models.ForeignKey('paiements.Paiement', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nom_document
