from django.db import models
from django.conf import settings

# --- Deposant ---
class Deposant(models.Model):
    id_dep = models.CharField(max_length=50, primary_key=True) # string dans [1]
    nom_dep = models.CharField(max_length=100)
    prenom_dep = models.CharField(max_length=100)
    denomination = models.CharField(max_length=255)
    adresse_dep = models.TextField()
    nationalite = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom_dep} {self.prenom_dep}"

# --- DemandeBrevet ---
class DemandeBrevet(models.Model):
    STATUT_CHOICES = [('valider', 'Valider'), ('non_valider', 'Non Valider')] # [1]

    id_demande = models.CharField(max_length=50, primary_key=True) # string dans [1]
    titre = models.CharField(max_length=1000)
    nature = models.CharField(max_length=100)
    num_depot = models.IntegerField()
    date_depot = models.DateField()
    pays_origine = models.CharField(max_length=100)
    numdemande_CA = models.IntegerField()
    date_CA = models.DateField()
    mandataire = models.CharField(max_length=255)
    date_pouvoir = models.DateField()
    prepose_reception = models.CharField(max_length=255)
    lieu_reception = models.CharField(max_length=255)
    date_reception = models.DateField()
    autre_info = models.TextField(blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='non_valider')

    # Relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # (1,1) dans [1]
    deposant = models.ForeignKey(Deposant, on_delete=models.CASCADE) # (1,1) dans [1]

    def __str__(self):
        return self.titre

# --- Inventeur ---
class Inventeur(models.Model):
    id_inv = models.CharField(max_length=50, primary_key=True) # string dans [1]
    nom_inv = models.CharField(max_length=100)
    prenom_inv = models.CharField(max_length=100)
    adresse_inv = models.TextField()
    # Relation (1,*) : Plusieurs inventeurs pour une demande [1]
    demande = models.ForeignKey(DemandeBrevet, on_delete=models.CASCADE, related_name='inventeurs')

    def __str__(self):
        return f"{self.nom_inv} {self.prenom_inv}"

# --- Brevet ---
class Brevet(models.Model):
    STATUS_CHOICES = [
        ('ACCEPTER', 'Accepter'),
        ('REFUSER', 'Refuser'),
        ('EN_ATTENTE', 'En attente'),
    ] # [1]

    id_brevet = models.CharField(max_length=50, primary_key=True) # string dans [1]
    num_brevet = models.IntegerField()
    titre = models.CharField(max_length=255)
    num_depot = models.IntegerField()
    date_depot = models.DateField()
    date_sortie = models.DateField()
    titulaire = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # Relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # (1,1) utilisateur peut créer (0,*) brevets [1]
    demande = models.OneToOneField(DemandeBrevet, on_delete=models.CASCADE, null=True, blank=True) # (0,1) dans [1]

    def __str__(self):
        return self.titre